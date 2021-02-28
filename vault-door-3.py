# char[] buffer = new char[32];
# int i;
# for (i=0; i < 8; i++)
# {
#   buffer[i] = password.charAt(i);
# }
# for (; i < 16; i++) {
#     buffer[i] = password.charAt(23 - i);
# }
# for (; i < 32; i += 2) {
#     buffer[i] = password.charAt(46 - i);
# }
# for (i=31; i >= 17; i -= 2) {
#     buffer[i] = password.charAt(i);
# }
# String s = new String(buffer);
# return s.equals("jU5t_a_sna_3lpm18gb41_u_4_mfr340");


if __name__ == '__main__':
    buffer = "jU5t_a_sna_3lpm18gb41_u_4_mfr340"
    password = [0] * 32
    for i in range(8):
        password[i] = buffer[i]

    for i in range(8, 16):
        password[23 - i] = buffer[i]

    for i in range(16, 32, 2):
        password[46 - i] = buffer[i]

    for i in range(31, 16, -2):
        password[i] = buffer[i]

    print("".join(password))
