"""Draw the two stacked-bar charts: good practices per attempt, and the second AI's marks.

Inputs (relative to the repository root):
    data/results.csv, data/scoring.json      the audited run records (commit b352093)
    research/ai-review-2026-09-10.json       the AI-assisted review of 10 September (not audited)

Outputs, written to figures/:
    exp-checks-stacked.png  + exp-checks-stacked.notes.txt  (the counts behind each bar)
    exp-review-stacked.png  + exp-review-stacked.notes.txt  (the mean marks behind each bar)

Run from anywhere:  uv run --no-project --with matplotlib python figures/make_stacked_figures.py
"""
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
FIGS = ROOT / "figures"
import json, csv, collections
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Patch
INK="#222222"; GREY="#6B7078"; LINE="#D5D7DC"; INDIGO="#4E51A5"
PAL=["#4E51A5","#eb6834","#1baf7a","#eda100","#e87ba4"]
plt.rcParams.update({"font.family":"Arial","font.size":13})
sc=json.load(open(DATA / "scoring.json")); rows={r["run"]:r for r in csv.DictReader(open(DATA / "results.csv"))}
LEVELS=[("L1","10 words"),("L2","46 words"),("L3","1,673 words")]
ORDER=["Opus 4.7","Opus 4.8","Opus 5","Fable 5.1","GPT-5.5","GPT-5.5 + note","GPT-5.6-Sol","GPT-5.6-Sol + note","GPT-6-Astra","GPT-6-Astra + note"]
LABEL={"Opus 4.7":"Claude Opus 4.7 (May model)","Opus 4.8":"Claude Opus 4.8","Opus 5":"Claude Opus 5","Fable 5.1":"Claude Fable 5.1","GPT-5.5":"GPT-5.5","GPT-5.5 + note":"GPT-5.5, with the note","GPT-5.6-Sol":"GPT-5.6-Sol","GPT-5.6-Sol + note":"GPT-5.6-Sol, with the note","GPT-6-Astra":"GPT-6-Astra","GPT-6-Astra + note":"GPT-6-Astra, with the note"}
def peek_kind(v):
    ts=v["test_selection"]; scope=str(v.get("leak_scope") or "")
    if ts=="leaked": return "headline" if scope.startswith("headline") else "other"
    return "none"
def stacked(panels, seg_names, fname, xlabel, notes_out, fmt="count", header=None):
    fig,axes=plt.subplots(1,3,figsize=(12.8,5.6),sharey=True)
    ypos={m:i for i,m in enumerate(ORDER)}
    notes=[]
    for ax,(lv,title),data in zip(axes,LEVELS,panels):
        ax.set_title(title,fontsize=17,color=INDIGO,loc="left",pad=10,fontweight="bold")
        for m in ORDER:
            y=ypos[m]
            if m not in data:
                ran=any(v["level"]==lv and v["model_label"]==m for v in sc.values())
                ax.text(0.08,y,"nothing delivered" if ran else "not run at this length",va="center",fontsize=10.5,color=GREY); continue
            vals,n=data[m]; left=0
            for j,v in enumerate(vals):
                if v>0:
                    ax.barh(y,v,left=left,height=0.62,color=PAL[j],edgecolor="white",linewidth=1.5); left+=v
            if left==0: ax.text(0.08,y,"nothing delivered",va="center",fontsize=10.5,color=GREY)
            else: ax.text(left+0.08,y,f"{left:.1f}",va="center",fontsize=11,color=INK)
            notes.append((title,m,n,vals))
        ax.set_xlim(0,5.6); ax.set_ylim(len(ORDER)-0.5,-0.6); ax.set_xticks([0,1,2,3,4,5]); ax.tick_params(axis="x",labelsize=12)
        ax.grid(axis="x",color=LINE,lw=0.6); ax.set_axisbelow(True)
        for s in ["top","right","left"]: ax.spines[s].set_visible(False)
        ax.tick_params(axis="y",length=0)
    axes[1].set_xlabel(xlabel,fontsize=13,color=GREY)
    axes[0].set_yticks(range(len(ORDER))); axes[0].set_yticklabels([LABEL[m] for m in ORDER],fontsize=14)
    handles=[Patch(facecolor=PAL[j],label=seg_names[j]) for j in range(5)]
    fig.legend(handles=handles,loc="lower center",ncol=3,frameon=False,fontsize=12,bbox_to_anchor=(0.5,0.0),columnspacing=1.3,handlelength=1.2)
    fig.subplots_adjust(left=0.23,right=0.98,top=0.9,bottom=0.28,wspace=0.1); fig.savefig(fname,dpi=170,facecolor="white"); plt.close(fig)
    with open(notes_out,"w") as f:
        if header: f.write(header+"\n")
        for title,m,n,vals in notes:
            if fmt=="count": f.write(f"- {title}, {LABEL[m]} ({n} attempts): "+"; ".join(f"{seg_names[j]} {vals[j]*n:.0f}/{n}" for j in range(5))+"\n")
            else: f.write(f"- {title}, {LABEL[m]} ({n} attempts): "+"; ".join(f"{seg_names[j]} {1+2*vals[j]:.1f}" for j in range(5))+"\n")

# ---- A: audit checks ----
CHECKS=[("Forecast itself did not peek",lambda v,r: r["source"]!="none" and peek_kind(v)!="headline"),
        ("Chose the method without the test score",lambda v,r: v["test_selection"]=="final_scoring_only"),
        ("Tested on past data first",lambda v,r: bool(v["validation"])),
        ("Gave a range",lambda v,r: bool(v["intervals"])),
        ("Wrote up its methods",lambda v,r: bool(v["methods_doc"]))]
panels=[]
for lv,_ in LEVELS:
    data={}
    for m in ORDER:
        vs=[(v,rows[k]) for k,v in sc.items() if v["level"]==lv and v["model_label"]==m]
        if not vs: continue
        data[m]=([sum(1 for v,r in vs if f(v,r))/len(vs) for _,f in CHECKS],len(vs))
    panels.append(data)
stacked(panels,[c[0] for c in CHECKS],FIGS / "exp-checks-stacked.png","Good practices found, out of 5 (average over that model's attempts)",FIGS / "exp-checks-stacked.notes.txt",
        header="# The counts behind figures/exp-checks-stacked.png: passed / attempts, from the 6 September 2026 audit's per-attempt fields (data/scoring.json and data/results.csv, commit b352093 of the experiment repository).")

# ---- B: AI review ----
rev=json.load(open(ROOT / "research" / "ai-review-2026-09-10.json"))["reviews"]
CATS=[("code_quality","Code quality"),("method_soundness","Sound method"),("honesty_of_reporting","Honest reporting"),("decision_quality","Good decisions"),("deliverables","Complete deliverables")]
panels=[]
for lv,_ in LEVELS:
    data={}
    for m in ORDER:
        rs=[r for r in rev if sc[r["run"]]["level"]==lv and sc[r["run"]]["model_label"]==m]
        if not rs: continue
        data[m]=([sum((r[k]-1)/2 for r in rs)/len(rs) for k,_ in CATS],len(rs))
    panels.append(data)
stacked(panels,[c[1] for c in CATS],FIGS / "exp-review-stacked.png","Second AI's marks, out of 5 (each point 0 = reject, 1 = accept; average over attempts)",FIGS / "exp-review-stacked.notes.txt",fmt="mean",
        header="# The mean marks (1 to 3) behind figures/exp-review-stacked.png: one Claude Opus 5 reviewer per attempt, 10 September 2026 (research/ai-review-2026-09-10.json). A second AI's reading, NOT checked by a person; the 6 September audit remains the authority.")
print("done")
