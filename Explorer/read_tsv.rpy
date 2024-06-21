if 't' not in vars():
    import sys,os;os.chdir('/Users/ryan/CleanCode/Projects/Adobe2023/PublicWebsite/Explorer');sys.path.append(os.getcwd())# CD ./Explorer
    t=pd.read_csv('magick_west2_defaultfilters.tsv','\t')

q=t[t.pipeline=='dfxl']
hand=q[q.tag_wrong_chosen==0][q.tag_very_incorrect==0 ][q.tag_incorrect==0 ][q.picked=='hand']
med=q[q.picked=='auto']
auto=med

auto=auto[auto.sim_score>median(auto.sim_score)]#Can't have 100000 on website...
ids=auto['download']
prompts=auto['subject']
ids=list(ids)
prompts=list(prompts)
ids+=list(hand.download)
ids=[x[len('dfxl/'):] for x in ids]#Like dfxl/YlgvxCf1Xa/outputs-strong_superkeylight.png
prompts+=list(hand.subject)


#Copy in ids and prompts to the html site