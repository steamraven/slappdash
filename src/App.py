from transcrypt import  wrap
exports = []  #__:skip 
require = None #__:skip

levenshtein = require('natural/lib/natural/distance/levenshtein_distance').LevenshteinDistanceSearch
draggable = require('vuedraggable')
AppButton = require('./components/AppButton')['default']
vue = require('vue')

data  =  [
    "Dimensions",
    "Banner",
    "AssetPanda",
    "Email",
    "El Sol",
    "TalentLMS",
    "Eagle Treasurer",
    "Eagle Assessor",
    "iWorks",
    "iCIMS",
    "Kryptos",
    "Alfresco",
    "BlueTeam",
    "Kronos",
    "RecordFusion",
    "RecordBook",
    "CivicClerk",
]

options = {
    "item": {
        "class": "item"
    },
    "bookmarks": {
        "group": {
            "name": 'bookmarks',  
            "put": True, 
        },
        "animation": 200,
        "item-key": lambda e: e,
        "direction": "horizontal",
        "class": "dash-bookmarkList dash-list",
    },
    "results": {
        "animation": 200,
        "sort": False,
        "item-key": lambda e: e,
        "group": {
            "name": 'results',
            "pull": 'clone',
            "put": False 
        },
        "class":"dash-resultList dash-list flex-wrap",
    },
    "trash": {
        "item-key": lambda e: e,
        "group": {
            "name": "trash",
            "put": True,
            "pull": False
        },
        "v-model": "trash",
        "v-on:add": "cleanTrash",
        "class":"dash-trash",
    },
    "newRow": {
        "item-key": lambda e: e,
        "group": {
            "name": "newRow",
            "put": True,
            "pull": False
        },
        "class":"dash-bookmarkList dash-list",
    }
}

def splitByLength(data, maxWidth, spacing):
    result = []
    current = []
    currentWidth = -spacing 
    for d in data:
        currentWidth += spacing 
        currentWidth += len(d['title'])
        if currentWidth <= maxWidth:
            current.append(d)
        else:
            result.append(current)
            current = [d]
            currentWidth = len(d['title'])
    if len(current):
        result.append(current)
    return result

def setup(props):

    bookmarks = vue.ref([])
    newRow = vue.ref([])
    bookmarkCount = vue.computed(lambda:
        sum(len(l) for l in bookmarks.value)
    )
    bookmarkNames = vue.computed(lambda: 
        [[i["name"] for i in l] for l in bookmarks.value]
    )

    def addBookmark():
        newBookmarks = newRow.value
        newRow.value = []
        bookmarks.value.append(newBookmarks)

    def cleanBookmarks():
        bookmarks.value = [l for l in bookmarks.value if len(l) > 0]


    trash = vue.ref([])
    def cleanTrash():
        trash.value = []

    dragBookmark = vue.ref(False)
    dragResult = vue.ref(False)

    showTrash = vue.computed(lambda: dragBookmark.value)

    hint = vue.computed( lambda: 
            "Drag Above to Bookmark" if dragResult.value or len(bookmarks.value) == 0 else
            "Drag Below to Remove Bookmark" if dragBookmark.value else
            ""
        )

    apps = vue.ref({ 
        d.lower(): {
            'name': d.lower(),
            'title': d
        } for d in data 
    })
    
    results = vue.computed( lambda: [a['name'] for a in sorted(apps.value.values(), lambda a: a['score'])])

    search = vue.ref("")

    def doSearch(newValue, oldValue):
        newValue = newValue.lower()
        for r in apps.value.values():
            d = levenshtein(newValue, r['name'])
            r.score = d.distance

    vue.watch(search, doSearch)

    return {
        "apps": apps,
        "results": results,

        "bookmarks": bookmarks,
        "newRow": newRow,

        "addBookmark": addBookmark,
        "cleanBookmarks": cleanBookmarks,

        "trash": trash,
        "cleanTrash": cleanTrash,

        "dragBookmark": dragBookmark,
        "dragResult": dragResult,
        "showTrash": showTrash,
        "hint": hint,


        "bookmarkCount": bookmarkCount,
        "bookmarkNames": bookmarkNames,

        "options": options,

        "search": search,
    }

exports['default'] = vue.defineComponent({
    "name": "App",
    "components": {
        "draggable": draggable,
        "AppButton": AppButton,

    },
    "setup": setup,
})