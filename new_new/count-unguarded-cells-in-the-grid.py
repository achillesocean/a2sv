class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        #hash the walls
        walls_dict = {}
        guards_dict = {}
        for guard in guards:
            temp = tuple(guard)
            guards_dict[temp] = 0
        for wall in walls:
            temp = tuple(wall)
            walls_dict[temp] = 0
            
        guarded = {}

        for guard in guards:
            r, c = guard[0] + 1, guard[1]
            while r < m:
                if (r, c) not in walls_dict and (r, c) not in guards_dict:
                    guarded[(r, c)] = 0
                else:
                    break
                r += 1
            r = guard[0] - 1
            while r >= 0:
                if (r, c) not in walls_dict and (r, c) not in guards_dict:
                    guarded[(r, c)] = 0
                else: 
                    break
                r -= 1
            r, c = guard[0], guard[1] - 1
            while c >= 0:
                if (r, c) not in walls_dict and (r, c) not in guards_dict:
                    guarded[(r, c)] = 0
                else: 
                    break
                c -= 1
            r, c = guard[0], guard[1] + 1
            while c < n:
                if (r, c) not in walls_dict and (r, c) not in guards_dict:
                    guarded[(r, c)] = 0
                else:
                    break
                c += 1
        tiles = m * n
        g_count = 0
        for key in guarded:
            g_count += 1
        print(guarded)
        return tiles - g_count - len(walls) - len(guards)
        
            
