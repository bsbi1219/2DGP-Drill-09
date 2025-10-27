# game 내의 객체들의 생성과 소멸을 관리하는 모듈입니다.

world = [] # 게임 내의 모든 객체를 담는 리스트

def add_object(o): # 게임 내에 객체를 추가하는 함수
    global world
    world.append(o)

def update(): # 게임 월드의 모든 객체들을 업데이트
    for o in world:
        o.update()

def render(): # 게임 월드의 모든 객체들을 그리기
    for o in world:
        o.draw()

