import imagematrix


class ResizeableImage(imagematrix.ImageMatrix):
    def best_seam(self):
        dp_table = [[(self.energy(i, j), 0) for j in range(self.height)]
                    for i in range(self.width)]
        def minim((i1, j1), (i2, j2), (i3, j3)):
            min_ = dp_table[i1][j1], i1
            if 0 <= i2 < self.width and dp_table[i2][j2] < min_[0] :
                min_ = dp_table[i2][j2], i2
            if 0 <= i3 < self.width and dp_table[i3][j3] < min_[0]:
                min_ = dp_table[i3][j3], i3
            return min_
        #print self.width, self.height, len(dp_table), len(dp_table[0])
        for j in range(1, self.height):
            for i in range(self.width):
                min_, ptr= minim((i, j - 1), (i - 1, j - 1), (i + 1, j - 1))
                dp_table[i][j] = dp_table[i][j][0] + min_[0], ptr
                
        min_, min_i= dp_table[0][self.height - 1], 0
        for i in range(self.width):
#            print dp_table[i][self.height - 1]
            if dp_table[i][self.height - 1] < min_:
                min_, min_i= dp_table[i][self.height - 1], i
                
        seam = [(min_i, self.height - 1)]
        ptr = min_[1]
        for j in range(self.height - 2, -1, -1):
            seam.append((ptr, j))
            ptr = dp_table[ptr][j][1]
        return seam
                
        
    def remove_best_seam(self):
        self.remove_seam(self.best_seam())
