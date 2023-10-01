let elements = document.querySelector('#insert').children;

new LeaderLine(
    document.getElementById('start'),
    LeaderLine.pointAnchor(elements.item(0), {
        x: 50,
        y: 50
    })
)

function loop(list, nextElem, startDirection, endDirection, side) {
    locSide = 100*side
    console.log(list)
    for (let i = 0; i < list.length; i++) {
        if (list.item(i).className == 'end') {return}
        // console.log(list.item(i))
        
        if (i < list.length) {
            if (list.item(i).className == 'ifWrapper') {
                if (i == list.length - 1) {
                    new LeaderLine(list.item(i), LeaderLine.pointAnchor(nextElem, {x: 0,y: 50}), {startLabel: 'false'})
                }
                else {
                    new LeaderLine(list.item(i), LeaderLine.pointAnchor(list.item(i+1), {x: 0,y: 50}), {startLabel: 'false'})
                }

                next = nextElem
                nextSearch: 
                for (let j = i + 1; j < list.length; j++) {
                    // if (list.item(j).className.indexOf('forWrapper') > -1) {

                    // }
                    if (list.item(j).className.indexOf('Wrapper') > -1 && list.item(j).children[0].getAttribute('data-parent') != list.item(i).children[1].getAttribute('data-parent')) {
                        next = list.item(j).children[0]
                        break nextSearch
                    }
                    else if (list.item(j).getAttribute('data-parent') != list.item(i).children[1].getAttribute('data-parent')) {
                        next = list.item(j)
                        break nextSearch
                    }
                }
                loop(list.item(i).children, next, 'right', 'right')
            }
            else if (list.item(i).className == 'whileWrapper') {
                new LeaderLine(list.item(i), LeaderLine.pointAnchor(list.item(i+1), {x: 0,y: 50}), {startLabel: 'false'})
                
                loop(list.item(i).children, list.item(i).children.item(0), 'top', 'top', 0.5)
            }
            else if (list.item(i).className == 'forWrapper') {
                if (i == list.length - 1) {
                    new LeaderLine(list.item(i), LeaderLine.pointAnchor(nextElem, {x: 0,y: 50}), {startLabel: 'After loop'})
                }
                else {
                    new LeaderLine(list.item(i), LeaderLine.pointAnchor(list.item(i+1), {x: 0,y: 50}), {startLabel: 'After Loop'})
                }

                loop(list.item(i).children, list.item(i).children.item(0), 'top', 'top', 0.5)
            }
            else if (list.item(i).className == 'while') {
                new LeaderLine(list.item(i), LeaderLine.pointAnchor(list.item(i+1), {x: 50,y: 50}), {startLabel: 'True'})

                
            }
            else if (list.item(i).className == 'for') {
                new LeaderLine(list.item(i), LeaderLine.pointAnchor(list.item(i+1), {x: 50,y: 50}), {startLabel: 'Loop'})
            }
            else if (list.item(i).className == 'if') {
                new LeaderLine(list.item(i), LeaderLine.pointAnchor(list.item(i+1), {x: 50,y: 50}), {startLabel: 'True'})

            }
            else { 
                if (i == list.length - 1) {
                    new LeaderLine(list.item(i), LeaderLine.pointAnchor(nextElem, {x: 50,y: 50})).setOptions({startScoket: startDirection, endSocket: endDirection})
                }
                else {
                    new LeaderLine(list.item(i), LeaderLine.pointAnchor(list.item(i+1), {x: 50,y: 50}))
                }
            }
        }
    };
}

loop(elements, document.getElementById('end'), 'right', 'right', 1)