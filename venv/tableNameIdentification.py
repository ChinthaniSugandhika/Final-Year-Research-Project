

table_synset_file = open('out/table_synset.txt', 'w')
def tableIdentifier(knowledgeBase, nounList):
    try:
        list = []
        n_list = []
        for n in nounList:
            syn = wordnet.synsets(n, pos='n')

            for a in knowledgeBase:
                for x in a[1]:
                    sim = x.wup_similarity(syn[0])
                    table_synset_file.write(str([n, syn[0], ':', x, '=', sim]))
                    table_synset_file.write("\n")

                    if sim >= 0.75:
                        list.append(a[0])
                        n_list.append(n)
                        return list, n_list
    except:
        tab, n_list = find_tables(nounList)
        return tab, n_list