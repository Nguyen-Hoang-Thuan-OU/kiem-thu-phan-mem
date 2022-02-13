package com.hoangthuan.mathutil.main;

import com.hoangthuan.mathutil.core.MathUtil;

public class Main {

    public static void main(String[] args) {

        // Kiểm thử thủ công (Manual Testing)
        
        // Ta kiểm thử bằng cách gọi hàm, truyền dữ liệu và chạy,
        // So sánh kết quả trả về (actual result)
        // với kết quả mong đợi (expected result)
        // ví dụ: 5!
        // 			- Mong đợi: 120
        // 			- Thực tế: hàm getFactorial(5) trả về = ?
        
        // Muốn thấy xuất hiện ngoại lệ hay không
        // thì cứ gọi để xem app bị "giết"
//        MathUtil.getFactorial(-5);
        
        // Để đảm bảo hàm đúng, ta phải chia các trường hợp,
        // nghĩ ra các tình huống có thể xảy ra
        // (nghĩa ra bộ dữ liệu để truyền vào hàm).
        
        // Mỗi bộ dữ liệu và dữ liệu cụ thể đưa vào
        // để kiểm thử hàm được gọi là Test Case.
        // Ví dụ:
        // 			n = -5 -> Test Case
        // 			n = 5 -> Test Case
        // Test case: tình huống kiểm thử (tình huống sử dụng)
        System.out.println("0! -> Mong đợi: 1; Thực tế: "
                + MathUtil.getFactorial(0));

        System.out.println("1! -> Mong đợi: 1; Thực tế: "
                + MathUtil.getFactorial(1));

        System.out.println("2! -> Mong đợi: 2; Thực tế: "
                + MathUtil.getFactorial(2));

        System.out.println("5! -> Mong đợi: 120; Thực tế: "
                + MathUtil.getFactorial(5));
    }

}
