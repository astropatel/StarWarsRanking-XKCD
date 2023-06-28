"""
This script creates an XKCD style plot of my personal qualitative
rankings of the major Star Wars "stories" -- from TV shows, to
all the movies.

Author: Rahul I. Patel: @DarthPatel

"""

import matplotlib.pyplot as plt

# SET UP DICTIONARY OF TEXT COLORS ASSOCIATED TO DIFFERENT MEDIA AND TYPES OF STORIES.
legend_dat = {'Main Films':      {'color':'tab:blue','ypos':2.1},
              'Star Wars Story': {'color':'tab:purple','ypos':1.7},
              'TV Show':        {'color':'tab:green','ypos':1.4},
              'Crap':           {'color':'tab:red','ypos':1.2}}

# SET UP DICTIONARY OF WHERE EACH STAR WARS STORY SHOULD GO IN A LOG SCALE
# Story Name: {'pos':value, 'type':value},...}
# 'pos' value = position on the vertical axis
# 'type' key from "colors" associated with type of story.
ENTData = {'Rogue One':
               {'pos': 1000, 'type': 'Star Wars Story'},

           'Ep V:\nEmpire Strikes Back':
               {'pos': 500, 'type': 'Main Films'},

           'Ep IV:\nA New Hope':
               {'pos': 400, 'type': 'Main Films'},

           'Ep VI:\nReturn of the Jedi':
               {'pos': 300, 'type': 'Main Films'},

           'The Mandalorian':
               {'pos': 250, 'type': 'TV Show'},

           'Clone Wars (2008)':
               {'pos': 150, 'type': 'TV Show'},

           'Clone Wars (2003)':
               {'pos': 120, 'type': 'TV Show'},

           'Rebels (2014)':
               {'pos': 100, 'type': 'TV Show'},

           'Ep VIII:\nThe Last Jedi':
               {'pos': 80, 'type': 'Main Films'},

           'Solo':
               {'pos': 55, 'type': 'Star Wars Story'},

           'Ep III:\nRevenge of the Sith':
               {'pos': 30, 'type': 'Main Films'},

           'Ep I:\nThe Phantom Menace':
               {'pos': 20, 'type': 'Main Films'},

           'Ep II:\nAttack of the Clones':
               {'pos': 15, 'type': 'Main Films'},

           'Ep VII:\nThe Force Awakens':
               {'pos': 8, 'type': 'Main Films'},

           'Ep IX:\n Rise of Skywalker':
               {'pos': 7, 'type': 'Main Films'},

           'Ewok & X-Mas stuff':
               {'pos': 1, 'type': 'Crap'}
           }
# START XKCD STYLE PLOT
with plt.xkcd():
    fig = plt.figure(figsize=(6,10))
    ax = fig.add_subplot(111)
    # REMOVE RIGHT, TOP, AND BOTTOM AXIS SPINES
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.spines['bottom'].set_color('none')
    # MOVE LEFT SPINE TO 0.01 ON THE X-AXIS
    ax.spines['left'].set_position(('data', 0.01))
    ax.spines['left'].set_linewidth(5)
    ax.spines['left'].set_linestyle('--')
    ax.spines['left'].set_color('grey')

    # ax.set_title('My\nSTAR WARS\nRankings\n',fontsize=18)
    ax.set_title('My\nSTAR WARS\nRankings - Story\n',fontsize=18)

    x = .5
    # offset = .5
    # PLOT EACH ELEMENT IN ENTDATA ONE BY ONE, ALTERNATING
    # THE X-POSITION OVER THE VERTICAL SPINE
    for movie, dat in ENTData.items():
        y = dat['pos']

        clr = legend_dat[dat['type']]['color']
        if x < 0:
            align = 'right'
        elif x > 0:
            align = 'left'
        ax.annotate(movie, xy=(.01, y), xycoords='data', xytext=(x * -1, y),textcoords='data',
                    size=8, va='center', ha=align, color='k',fontsize=12,
                    arrowprops=dict(arrowstyle='->', lw=2.5, color=clr),
                    bbox=dict(facecolor=clr, edgecolor=clr,
                              boxstyle='round', pad=0.5, alpha=0.4)
                    )

        x *= -1
        ax.plot(x, y, 'o', ms=0)

    ewok = ENTData['Ewok & X-Mas stuff']
    posewok = ewok['pos']
    ax.annotate("Didn't see 'em.\nWon't see 'em.", xy=(.375, 1.09), xycoords='data',
                xytext=(.5, posewok + .8), textcoords='data',
                size=8, va='center', ha=align, color='k',
                arrowprops=dict(arrowstyle='-', lw=1, color='k', alpha=0.6),
                alpha=0.6
                )

    ax.annotate("BEST", xy=(.05, 1000),
                xytext=(0.25, 1200), textcoords='data',
                size=16, va='center', ha=align, color='k', alpha=0.6
                )

    ax.annotate("Just... no.", xy=(0.01, 0.8),
                xytext=(0.01, 0.8), textcoords='data',
                size=16, va='center', ha=align, color='k', alpha=0.6
                )

    ax.annotate("Rahul I. Patel \n @DarthPatel", xy=(0.5, 1000),
                xytext=(0.5, 1000), textcoords='data',
                size=6, va='center', ha=align, color='k', alpha=0.6
                )
    
    ax.annotate("Legend", xy=(-0.52, 2.6),
            xytext=(-0.52,2.6), textcoords='data',
            size=10, va='center', color='k', alpha=0.6
            )
    for lab,coldat in legend_dat.items():
        y = coldat['ypos']
        ax.annotate(lab, xy=(-0.5, y), xycoords='data', xytext=(-0.5, y),
                    textcoords='data',size=8, va='center', color='k',fontsize=8,
                    bbox=dict(facecolor=coldat['color'], edgecolor=coldat['color'],
                              boxstyle='round', pad=0.5, alpha=0.4)
                    )
    
    plt.semilogy()
    plt.yticks([])
    plt.xticks([])
    plt.tight_layout()
    #plt.savefig('StarWarsOrdering_09192021.png', dpi=250)
    plt.show()
