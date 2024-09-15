TOTAL_DISKS = 10

TOWERS = {
    'A': list(reversed(range(1, TOTAL_DISKS + 1))),
    'B': [],
    'C': [],
}

def printDisk(diskNum: int) -> None:
    emptySpace = ' ' * (TOTAL_DISKS - diskNum)
    if diskNum == 0:
        print(emptySpace + '||' + emptySpace, end='')
    else:
        diskSpace = '@' * diskNum
        diskNumLabel = str(diskNum).rjust(2, '_')
        print(emptySpace + diskSpace + diskNumLabel + diskSpace + emptySpace, end='')
        
def printTowers() -> None:
    for level in range(TOTAL_DISKS, -1, -1):
        for tower in (TOWERS['A'], TOWERS['B'], TOWERS['C']):
            if level >= len(tower):
                printDisk(0)
            else:
                printDisk(tower[level])
        print()
    
    emptySpace = ' ' * (TOTAL_DISKS)
    print(emptySpace + 'A' + emptySpace + emptySpace + 'B' + emptySpace + emptySpace + 'C' + emptySpace)
    
def moveOneDisk(startTower: str, endTowerr: str) -> None:
    disk = TOWERS[startTower].pop()
    TOWERS[endTowerr].append(disk)
    
def solve(numberOfDisks: int, startTower: str, tempTower: str, endTower: str) -> None:
    if numberOfDisks == 1:
        moveOneDisk(startTower, endTower)
        printTowers()
        return
    else:
        solve(numberOfDisks - 1, startTower, endTower, tempTower)
        moveOneDisk(startTower, endTower)
        printTowers()
        solve(numberOfDisks - 1, tempTower, startTower, endTower)
        return
    
printTowers()
solve(TOTAL_DISKS, 'A', 'B', 'C')
    
        