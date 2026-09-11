"""Draw the experiment charts from the audited run records.

Inputs (relative to the repository root):
    data/results.csv    one row per attempt: recomputed score, source, alignment
    data/scoring.json   the 6 September audit's per-attempt fields
Both are copies of runs_2026_09/ at commit b352093 of the experiment repository.

Outputs, written to figures/ (the deck uses exp-all-levels.png, exp-stopped.png
and exp-coverage.png; the rest are companion charts):
    exp-every-attempt.png, exp-report-card.png, exp-stopped.png, exp-coverage.png,
    exp-report-card-{10,46,1673}-words.png, exp-attempts-{10,46,1673}-words.png,
    exp-all-levels.png

Run from anywhere:  uv run --no-project --with matplotlib python figures/make_experiment_figures.py
"""
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
FIGS = ROOT / "figures"
SLUG = {"L1": "10-words", "L2": "46-words", "L3": "1673-words"}
import json, csv, collections, math
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from matplotlib.patches import Patch

INDIGO="#4E51A5"; PERI="#8294F3"; SKY="#45B9EB"; TEAL="#64D3D4"; GOLD="#EAC04B"; CORAL="#FF8179"; GREY="#6B7078"; LINE="#D5D7DC"; INK="#222222"
plt.rcParams.update({"font.family":"Arial","font.size":13,"axes.edgecolor":LINE,"axes.labelcolor":INK,"xtick.color":INK,"ytick.color":INK,"axes.titlecolor":INK})

sc=json.load(open(DATA / "scoring.json")); rows={r["run"]:r for r in csv.DictReader(open(DATA / "results.csv"))}
LEVELS=[("L1","10 words"),("L2","46 words"),("L3","1,673 words")]
ORDER=["Opus 4.7","Opus 4.8","Opus 5","Fable 5.1","GPT-5.5","GPT-5.5 + note","GPT-5.6-Sol","GPT-5.6-Sol + note","GPT-6-Astra","GPT-6-Astra + note"]
LABEL={"Opus 4.7":"Claude Opus 4.7 (the May model)","Opus 4.8":"Claude Opus 4.8","Opus 5":"Claude Opus 5","Fable 5.1":"Claude Fable 5.1","GPT-5.5":"GPT-5.5","GPT-5.5 + note":"GPT-5.5, with the note","GPT-5.6-Sol":"GPT-5.6-Sol","GPT-5.6-Sol + note":"GPT-5.6-Sol, with the note","GPT-6-Astra":"GPT-6-Astra","GPT-6-Astra + note":"GPT-6-Astra, with the note"}

def peek_kind(v):
    ts=v["test_selection"]; scope=str(v.get("leak_scope") or "")
    if ts=="leaked": return "headline" if scope.startswith("headline") else "other"
    return "none"

# ---------- Figure 1: every scored attempt ----------
fig,axes=plt.subplots(1,3,figsize=(13,5.4),sharey=True)
ylabels=["Opus 4.7, May"]+ORDER
ypos={m:i for i,m in enumerate(ylabels)}
may={"L1":(10.76,"none"),"L2":(5.52,"none"),"L3":(3.43,"headline")}
for ax,(lv,title) in zip(axes,LEVELS):
    ax.set_title(title,fontsize=14,color=INDIGO,loc="left",pad=8)
    ax.axvspan(-1,13,color="white")
    for i in range(len(ylabels)):
        ax.axhline(i,color=LINE,lw=0.6,zorder=0)
    # may point
    x,pk=may[lv]; ax.scatter([x],[ypos["Opus 4.7, May"]],s=70,marker="o",facecolor=(CORAL if pk=="headline" else INDIGO),edgecolor="white",linewidth=1.2,zorder=3)
    noscore=collections.Counter()
    for k,v in sc.items():
        if v["level"]!=lv: continue
        r=rows[k]; m=v["model_label"]; y=ypos[m]
        if r["source"]=="none": noscore[m]+=1; continue
        x=float(r["mape_pct"]) if r["mape_pct"] else float(v["agent_reported_mape"])
        pk=peek_kind(v); col={"headline":CORAL,"other":GOLD,"none":INDIGO}[pk]
        if r["source"]=="recomputed": ax.scatter([x],[y],s=70,marker="o",facecolor=col,edgecolor="white",linewidth=1.2,zorder=3)
        else: ax.scatter([x],[y],s=80,marker="D",facecolor="white",edgecolor=col,linewidth=2,zorder=3)
    for m,c in noscore.items():
        ax.text(12.3,ypos[m],f"no score ×{c}",va="center",ha="right",fontsize=10,color=GREY)
    ax.set_xlim(0,12.5); ax.set_ylim(len(ylabels)-0.5,-0.5)
    ax.set_xlabel("Average error, % (lower is better)",fontsize=11,color=GREY)
    ax.tick_params(axis="x",labelsize=11); ax.grid(axis="x",color=LINE,lw=0.6); ax.set_axisbelow(True)
    for s in ["top","right"]: ax.spines[s].set_visible(False)
axes[0].set_yticks(range(len(ylabels))); axes[0].set_yticklabels([LABEL.get(m,m) for m in ylabels],fontsize=11)
handles=[Line2D([],[],marker="o",color="w",markerfacecolor=INDIGO,markersize=9,label="Fair forecast, score checked by us"),
         Line2D([],[],marker="D",color="w",markeredgecolor=INDIGO,markerfacecolor="white",markeredgewidth=2,markersize=9,label="The assistant's own number, not rechecked"),
         Line2D([],[],marker="o",color="w",markerfacecolor=CORAL,markersize=9,label="The forecast itself peeked at the target week"),
         Line2D([],[],marker="o",color="w",markerfacecolor=GOLD,markersize=9,label="Peeked while choosing or checking, forecast itself clean")]
fig.legend(handles=handles,loc="lower center",ncol=2,frameon=False,fontsize=11,bbox_to_anchor=(0.5,-0.02))
fig.tight_layout(rect=(0,0.09,1,1)); fig.savefig(FIGS / "exp-every-attempt.png",dpi=170,facecolor="white"); plt.close(fig)

# ---------- Figure 2: report card ----------
CRIT=[("Delivered a scored forecast",lambda v,r: r["source"]!="none"),
      ("Score checked by us",lambda v,r: r["source"]=="recomputed"),
      ("Forecast itself did not peek",lambda v,r: r["source"]!="none" and peek_kind(v)!="headline"),
      ("Chose the method without the test score",lambda v,r: v["test_selection"]=="final_scoring_only"),
      ("Tested on past data before choosing",lambda v,r: bool(v["validation"])),
      ("Gave a range showing how sure it was",lambda v,r: bool(v["intervals"])),
      ("Wrote up its methods",lambda v,r: bool(v["methods_doc"])),
      ("Finished without interruption",lambda v,r: not v.get("status_note"))]
from matplotlib.colors import LinearSegmentedColormap
cmap=LinearSegmentedColormap.from_list("ind",["#F3F3FA","#C9CBEA",INDIGO])
fig,axes=plt.subplots(1,3,figsize=(15,6.2),sharey=False)
for ax,(lv,title) in zip(axes,LEVELS):
    models=[m for m in ORDER if any(v["level"]==lv and v["model_label"]==m for v in sc.values())]
    grid=[]; txt=[]
    for m in models:
        vs=[(v,rows[k]) for k,v in sc.items() if v["level"]==lv and v["model_label"]==m]
        n=len(vs); rowv=[]; rowt=[]
        for name,f in CRIT:
            k=sum(1 for v,r in vs if f(v,r)); rowv.append(k/n); rowt.append(f"{k}/{n}")
        grid.append(rowv); txt.append(rowt)
    im=ax.imshow(grid,cmap=cmap,vmin=0,vmax=1,aspect="auto")
    ax.set_xticks(range(len(CRIT))); ax.set_xticklabels([c[0] for c in CRIT],rotation=40,ha="right",fontsize=9.5)
    ax.set_yticks(range(len(models))); ax.set_yticklabels([LABEL.get(m,m) for m in models],fontsize=10)
    for i in range(len(models)):
        for j in range(len(CRIT)):
            ax.text(j,i,txt[i][j],ha="center",va="center",fontsize=10,color=("white" if grid[i][j]>0.6 else INK))
    ax.set_title(title,fontsize=14,color=INDIGO,loc="left",pad=8)
    for s in ax.spines.values(): s.set_visible(False)
    ax.tick_params(length=0)
    # white gridlines
    ax.set_xticks([x-0.5 for x in range(1,len(CRIT))],minor=True); ax.set_yticks([y-0.5 for y in range(1,len(models))],minor=True)
    ax.grid(which="minor",color="white",lw=2); ax.tick_params(which="minor",length=0)
fig.suptitle("Report card: how many of each model's attempts met each check (from the 6 September audit)",x=0.01,ha="left",fontsize=15,color=INK)
fig.tight_layout(rect=(0,0,1,0.95)); fig.savefig(FIGS / "exp-report-card.png",dpi=170,facecolor="white"); plt.close(fig)

# ---------- Figure 3: stopped to ask ----------
fig,ax=plt.subplots(figsize=(11,4.6))
groups=[("GPT-6-Astra",9,9),("GPT-5.6-Sol",6,9),("GPT-5.5",5,9),("All three, with the note",0,20)]
for i,(name,stopped,n) in enumerate(groups):
    ax.barh(i,n-stopped,color=INDIGO,height=0.55,label="Went on with the task" if i==0 else None)
    ax.barh(i,stopped,left=n-stopped+0.0,color=GOLD,height=0.55,label="Stopped to ask a question or propose a plan" if i==0 else None,edgecolor="white",linewidth=2)
    ax.text(n+0.3,i,f"{stopped} of {n} stopped",va="center",fontsize=14,color=INK)
ax.set_yticks(range(len(groups))); ax.set_yticklabels([g[0] for g in groups],fontsize=15); ax.invert_yaxis()
ax.set_xlim(0,24); ax.set_xlabel("Attempts",fontsize=11,color=GREY)
for s in ["top","right","left"]: ax.spines[s].set_visible(False)
ax.tick_params(axis="y",length=0); ax.grid(axis="x",color=LINE,lw=0.6); ax.set_axisbelow(True)
ax.legend(loc="upper center",bbox_to_anchor=(0.5,1.16),ncol=2,frameon=False,fontsize=13)
fig.tight_layout(); fig.savefig(FIGS / "exp-stopped.png",dpi=170,facecolor="white"); plt.close(fig)

# ---------- Figure 4: coverage ----------
fig,ax=plt.subplots(figsize=(11,3.6))
cov={"80% range":(80,[57.1,50.6,48.8]),"95% range":(95,[94.0,91.7,83.3])}
for i,(lab,(nom,vals)) in enumerate(cov.items()):
    ax.plot([nom,nom],[i-0.3,i+0.3],color=GREY,lw=2,ls="--")
    ax.scatter(vals,[i]*3,s=140,color=INDIGO,edgecolor="white",linewidth=1.2,zorder=3)
    ax.text(nom,i-0.38,f"label: {nom}%",ha="center",fontsize=13,color=GREY)
ax.set_yticks([0,1]); ax.set_yticklabels(list(cov.keys()),fontsize=15); ax.set_ylim(1.6,-0.7)
ax.set_xlim(40,103); ax.set_xlabel("How often the range contained the true value, % of the 168 test hours",fontsize=11,color=GREY)
for s in ["top","right","left"]: ax.spines[s].set_visible(False)
ax.tick_params(axis="y",length=0); ax.grid(axis="x",color=LINE,lw=0.6); ax.set_axisbelow(True)
fig.tight_layout(); fig.savefig(FIGS / "exp-coverage.png",dpi=170,facecolor="white"); plt.close(fig)
print("figures written")

# ---------- Figure 2b: report card, one file per level ----------
for lv,title in LEVELS:
    models=[m for m in ORDER if any(v["level"]==lv and v["model_label"]==m for v in sc.values())]
    grid=[]; txt=[]
    for m in models:
        vs=[(v,rows[k]) for k,v in sc.items() if v["level"]==lv and v["model_label"]==m]
        n=len(vs); rowv=[]; rowt=[]
        for name,f in CRIT:
            k=sum(1 for v,r in vs if f(v,r)); rowv.append(k/n); rowt.append(f"{k}/{n}")
        grid.append(rowv); txt.append(rowt)
    fig,ax=plt.subplots(figsize=(13,5.4))
    ax.imshow(grid,cmap=cmap,vmin=0,vmax=1,aspect="auto")
    SHORT=["Delivered\na score","Checked\nby us","Forecast\ndid not peek","Chose without\ntest score","Tested on\npast data","Gave a\nrange","Wrote up\nits methods","Finished"]
    ax.set_xticks(range(len(CRIT))); ax.set_xticklabels(SHORT,fontsize=14); ax.xaxis.tick_top(); ax.xaxis.set_label_position("top")
    ax.set_yticks(range(len(models))); ax.set_yticklabels([LABEL.get(m,m) for m in models],fontsize=15)
    for i in range(len(models)):
        for j in range(len(CRIT)):
            ax.text(j,i,txt[i][j],ha="center",va="center",fontsize=16,color=("white" if grid[i][j]>0.6 else INK))
    for s in ax.spines.values(): s.set_visible(False)
    ax.tick_params(length=0)
    ax.set_xticks([x-0.5 for x in range(1,len(CRIT))],minor=True); ax.set_yticks([y-0.5 for y in range(1,len(models))],minor=True)
    ax.grid(which="minor",color="white",lw=2.5); ax.tick_params(which="minor",length=0)
    fig.tight_layout(); fig.savefig(FIGS / f"exp-report-card-{SLUG[lv]}.png",dpi=170,facecolor="white"); plt.close(fig)
print("per-level cards written")

# ---------- Figure 5: per-level dot charts (replace the three tables) ----------
for lv,title in LEVELS:
    models=[m for m in ORDER if any(v["level"]==lv and v["model_label"]==m for v in sc.values())]
    ylabels=["Opus 4.7, May"]+models; ypos={m:i for i,m in enumerate(ylabels)}
    fig,ax=plt.subplots(figsize=(13,5.6))
    for i in range(len(ylabels)): ax.axhline(i,color=LINE,lw=0.6,zorder=0)
    x,pk=may[lv]; ax.scatter([x],[0],s=150,marker="o",facecolor=(CORAL if pk=="headline" else INDIGO),edgecolor="white",linewidth=1.5,zorder=3)
    noscore=collections.Counter()
    for k,v in sc.items():
        if v["level"]!=lv: continue
        r=rows[k]; m=v["model_label"]; y=ypos[m]
        if r["source"]=="none": noscore[m]+=1; continue
        x=float(r["mape_pct"]) if r["mape_pct"] else float(v["agent_reported_mape"])
        pk=peek_kind(v)
        col={"headline":CORAL,"other":GOLD,"none":INDIGO}[pk]
        if v["test_selection"]=="indeterminate": col=GREY
        ended=bool(v.get("status_note"))
        if r["source"]=="recomputed": ax.scatter([x],[y],s=150,marker="o",facecolor=col,edgecolor="white",linewidth=1.5,zorder=3)
        else: ax.scatter([x],[y],s=170,marker="D",facecolor="white",edgecolor=col,linewidth=2.4,zorder=3)
        if ended: ax.scatter([x],[y],s=420,marker="o",facecolor="none",edgecolor=INK,linewidth=1.2,zorder=2)
    xmax={"L1":12.5,"L2":10.5,"L3":7.5}[lv]
    for m,c in noscore.items():
        ax.text(xmax-0.1,ypos[m],f"no score ×{c}",va="center",ha="right",fontsize=13,color=GREY)
    ax.set_xlim(0,xmax); ax.set_ylim(len(ylabels)-0.5,-0.7)
    ax.set_yticks(range(len(ylabels))); ax.set_yticklabels([LABEL.get(m,m) for m in ylabels],fontsize=15)
    ax.set_xlabel("Average error, % (lower is better)",fontsize=14,color=GREY); ax.tick_params(axis="x",labelsize=13)
    for s in ["top","right","left"]: ax.spines[s].set_visible(False)
    ax.tick_params(axis="y",length=0); ax.grid(axis="x",color=LINE,lw=0.6); ax.set_axisbelow(True)
    handles=[Line2D([],[],marker="o",color="w",markerfacecolor=INDIGO,markersize=11,label="Fair, checked by us"),
             Line2D([],[],marker="D",color="w",markeredgecolor=INDIGO,markerfacecolor="white",markeredgewidth=2.4,markersize=10,label="The assistant's own number"),
             Line2D([],[],marker="o",color="w",markerfacecolor=CORAL,markersize=11,label="The forecast itself peeked"),
             Line2D([],[],marker="o",color="w",markerfacecolor=GOLD,markersize=11,label="Peeked while choosing or checking"),
             Line2D([],[],marker="o",color="w",markerfacecolor=GREY,markersize=11,label="The audit could not decide"),
             Line2D([],[],marker="o",color="w",markerfacecolor="white",markeredgecolor=INK,markeredgewidth=1.2,markersize=16,label="Attempt ended early")]
    ax.legend(handles=handles,loc="lower center",bbox_to_anchor=(0.5,-0.36),ncol=3,frameon=False,fontsize=13)
    fig.tight_layout(); fig.savefig(FIGS / f"exp-attempts-{SLUG[lv]}.png",dpi=170,facecolor="white"); plt.close(fig)
print("per-level dot charts written")

# ---------- Figure 6: three panels, shared axis, slide proportions ----------
fig,axes=plt.subplots(1,3,figsize=(12.8,5.6),sharey=True)
ylabels=["Opus 4.7, May"]+ORDER; ypos={m:i for i,m in enumerate(ylabels)}
for ax,(lv,title) in zip(axes,LEVELS):
    ax.set_title(title,fontsize=17,color=INDIGO,loc="left",pad=10,fontweight="bold")
    for i in range(len(ylabels)): ax.axhline(i,color=LINE,lw=0.6,zorder=0)
    x,pk=may[lv]; ax.scatter([x],[0],s=95,marker="o",facecolor=(CORAL if pk=="headline" else INDIGO),edgecolor="white",linewidth=1.3,zorder=3)
    noscore=collections.Counter()
    for k,v in sc.items():
        if v["level"]!=lv: continue
        r=rows[k]; m=v["model_label"]; y=ypos[m]
        if r["source"]=="none": noscore[m]+=1; continue
        x=float(r["mape_pct"]) if r["mape_pct"] else float(v["agent_reported_mape"])
        pk=peek_kind(v); col={"headline":CORAL,"other":GOLD,"none":INDIGO}[pk]
        if v["test_selection"]=="indeterminate": col=GREY
        if r["source"]=="recomputed": ax.scatter([x],[y],s=95,marker="o",facecolor=col,edgecolor="white",linewidth=1.3,zorder=3)
        else: ax.scatter([x],[y],s=105,marker="D",facecolor="white",edgecolor=col,linewidth=2,zorder=3)
    for m,c in noscore.items():
        ax.text(12.6,ypos[m],f"no score ×{c}",va="center",ha="right",fontsize=11,color=GREY)
    ax.set_xlim(0,12.8); ax.set_ylim(len(ylabels)-0.5,-0.6); ax.set_xticks([0,4,8,12]); ax.tick_params(axis="x",labelsize=13)
    ax.grid(axis="x",color=LINE,lw=0.6); ax.set_axisbelow(True)
    for s in ["top","right","left"]: ax.spines[s].set_visible(False)
    ax.tick_params(axis="y",length=0)
axes[1].set_xlabel("Average error, % (lower is better)",fontsize=14,color=GREY)
axes[0].set_yticks(range(len(ylabels))); SHORTL=dict(LABEL); SHORTL["Opus 4.7"]="Claude Opus 4.7 (May model)"
axes[0].set_yticklabels([SHORTL.get(m,m) for m in ylabels],fontsize=14)
handles=[Line2D([],[],marker="o",color="w",markerfacecolor=INDIGO,markersize=10,label="Fair, checked by us"),
         Line2D([],[],marker="D",color="w",markeredgecolor=INDIGO,markerfacecolor="white",markeredgewidth=2,markersize=9,label="The assistant's own number"),
         Line2D([],[],marker="o",color="w",markerfacecolor=CORAL,markersize=10,label="The forecast itself peeked"),
         Line2D([],[],marker="o",color="w",markerfacecolor=GOLD,markersize=10,label="Peeked while choosing or checking"),
         Line2D([],[],marker="o",color="w",markerfacecolor=GREY,markersize=10,label="Audit could not decide")]
fig.legend(handles=handles,loc="lower center",ncol=3,frameon=False,fontsize=12.5,bbox_to_anchor=(0.5,0.0),columnspacing=1.4)
fig.subplots_adjust(left=0.24,right=0.98,top=0.9,bottom=0.28,wspace=0.1); fig.savefig(FIGS / "exp-all-levels.png",dpi=170,facecolor="white"); plt.close(fig)
print("combined written")
