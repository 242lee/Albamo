def solution(points, routes):
    # 각 포인트의 좌표를 쉽게 참조하기 위한 딕셔너리
    point_coords = {i + 1: tuple(coord) for i, coord in enumerate(points)}
    
    def get_path(start_point, end_point):
        """두 포인트 사이의 최단 경로를 반환하는 함수"""
        start_r, start_c = point_coords[start_point]
        end_r, end_c = point_coords[end_point]
        path = []
        curr_r, curr_c = start_r, start_c
        
        # r 좌표 먼저 이동
        while curr_r != end_r:
            curr_r += 1 if end_r > curr_r else -1
            path.append((curr_r, curr_c))
        
        # c 좌표 이동
        while curr_c != end_c:
            curr_c += 1 if end_c > curr_c else -1
            path.append((curr_r, curr_c))
            
        # 도착 지점도 경로에 포함
        if path and path[-1] != (end_r, end_c):
            path.append((end_r, end_c))
            
        # 출발지와 도착지가 같은 경우
        if not path and start_point == end_point:
            path.append((start_r, start_c))
            
        return path

    def get_robot_positions(route):
        """각 로봇의 전체 이동 경로를 계산하는 함수"""
        positions = []
        for i in range(len(route) - 1):
            # 첫 위치를 포함
            if i == 0:
                positions.append(point_coords[route[0]])
            path = get_path(route[i], route[i + 1])
            positions.extend(path)
        return positions

    # 각 로봇의 전체 이동 경로 계산
    robot_paths = [get_robot_positions(route) for route in routes]
    
    # 가장 긴 경로의 길이 찾기
    max_time = max(len(path) for path in robot_paths)
    
    danger_count = 0
    
    # 각 시간대별로 위험 상황 체크
    for t in range(max_time):
        # 현재 시간의 각 로봇 위치 수집
        current_positions = {}
        
        for robot_id, path in enumerate(robot_paths):
            if t < len(path):  # 아직 운송 중인 로봇만 체크
                pos = path[t]
                if pos in current_positions:
                    current_positions[pos].append(robot_id)
                else:
                    current_positions[pos] = [robot_id]
        
        # 위험 상황 카운트
        for pos, robots in current_positions.items():
            if len(robots) >= 2:  # 같은 위치에 2대 이상의 로봇이 있는 경우
                danger_count += 1
    
    return danger_count
