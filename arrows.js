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
    for (let i = 0; i < list.length; i++) {
        console.log(list.item(i))
        
        if (i + 1 < list.length) {
            if (list.item(i).className == 'ifWrapper') {

                new LeaderLine(list.item(i), LeaderLine.pointAnchor(list.item(i+1), {x: 0,y: 50}), {startLabel: 'false'})

                

                for (let j = i; j < list.length; j++) {
                    if (list.item(j).getAttribute('data-parent') != list.item(i).getAttribute('data-parent')) {
                        next = list.item(j)
                    }
                }
                loop(list.item(i).children, next, 'right', 'right')
            }
            else if (list.item(i).className == 'whileWrapper') {
                new LeaderLine(list.item(i), LeaderLine.pointAnchor(list.item(i+1), {x: 0,y: 50}), {startLabel: 'false'})
                
                loop(list.item(i).children, list.item(i).children.item(0), 'top', 'top', 0.5)
            }
            else if (list.item(i).className == 'while') {
                new LeaderLine(list.item(i), LeaderLine.pointAnchor(list.item(i+1), {x: 50,y: 50}), {startLabel: 'True'})

                
            }
            else if (list.item(i).className == 'if') {
                new LeaderLine(list.item(i), LeaderLine.pointAnchor(list.item(i+1), {x: 50,y: 50}), {startLabel: 'True'})

            }
            else { 
                new LeaderLine(list.item(i), LeaderLine.pointAnchor(list.item(i+1), {x: 50,y: 50}))
            }
        }
    };
        
    new LeaderLine(list.item(list.length -1 ), LeaderLine.pointAnchor(nextElem, {x: locSide})).setOptions({startSocket: startDirection, endSocket:endDirection})
}

loop(elements, document.getElementById('end'), 'right', 'right', 1)