package com.hoangthuan.mathutil.core;

import static com.hoangthuan.mathutil.core.MathUtil.getFactorial;
import org.junit.Test;
import static org.junit.Assert.*;
import org.junit.runner.RunWith;
import org.junit.runners.Parameterized;
import org.junit.runners.Parameterized.Parameter;
import org.junit.runners.Parameterized.Parameters;

// Báo cho máy ảo Java (JUNit) rằng class này là class tham số hoá
@RunWith(value = Parameterized.class)
public class AdvancedFactorialTest {
    
    // Tách toàn bộ dữ liệu cần test
    // gồm đầu vào và đầu ra sang một chỗ
    // (có thể là một file text, csv, excel, database,... riêng)
    // để dễ quản lý và đảm bảo đã bao đủ hết các trường hợp
    // (đây là được xem là Test Script tự động)
    
    // Tên hàm được đặt tự do
    // Khai báo tập hợp các tham số,
    // hàm trả về mảng 2 chiều kiểu Object
    // vì các framework sẽ chơi với Object,
    // mảng số nguyên cũng phải hiểu là đối tượng,
    // tức là chơi với Wrapper Class* nếu là mảng số
    // * Wrapper Class: Integer (int), Character (char),...
    
    // Báo cho máy ảo Java (JUNit) biết đây là dữ liệu nguồn,
    // dùng để truyền vào hàm assert
    @Parameters
    public static Object[][] initData() {
        return new Integer[][] {
                                {0, 1},
                                {1, 1},
                                {2, 2},
                                {3, 6},
                                {4, 24},
                                {5, 120},
                                {6, 720}
                               };
    }
    
    // Chuẩn bị 2 biến để hứng bộ dữ liệu từ mảng theo từng cặp,
    // sau đó đưa cặp (input + expected) vào hàm test
    
    // Ánh xạ input với cột 0
    @Parameter(value = 0)
    public int input;
    
    // Ánh xạ expected với cột 1
    @Parameter(value = 1)
    public long expected;
    
    // Nhận bộ dữ liệu kiểm thử và tự động tiến hành kiểm thử
    @Test
    public void checkFactorialGivenCorrectArgumentReturnWell() {

        //long actual = getFactorial(input);
        assertEquals(expected, getFactorial(input));
    }
}