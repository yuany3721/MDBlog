---
title: 'RSA'
date: Sun, 29 Aug 2021 02:35:40 +0000
draft: false
tags: ['RSA', '公钥密码', '密码学', '非对称密码']
---

> RSA (Rivest–Shamir–Adleman) is a public-key cryptosystem that is widely used for secure data transmission. It is also one of the oldest. The acronym RSA comes from the surnames of Ron Rivest, Adi Shamir and Leonard Adleman, who publicly described the algorithm in 1977. An equivalent system was developed secretly, in 1973 at GCHQ (the British signals intelligence agency), by the English mathematician Clifford Cocks. That system was declassified in 1997. In a public-key cryptosystem, the encryption key is public and distinct from the decryption key, which is kept secret (private). An RSA user creates and publishes a public key based on two large prime numbers, along with an auxiliary value. The prime numbers are kept secret. Messages can be encrypted by anyone, via the public key, but can only be decoded by someone who knows the prime numbers. The security of RSA relies on the practical difficulty of factoring the product of two large prime numbers, the factoring problem. Breaking RSA encryption is known as the RSA problem. Whether it is as difficult as the factoring problem is an open question. There are no published methods to defeat the system if a large enough key is used. RSA is a relatively slow algorithm. Because of this, it is not commonly used to directly encrypt user data. More often, RSA is used to transmit shared keys for symmetric key cryptography, which are then used for bulk encryption-decryption.

Operation
---------

### 密钥生成

1.  选择两个不同素数p和q
    *   出于安全目的，p和q应该随机选择，并且应该在大小上相似但长度相差几个数字，以使分解更加困难
    *   p和q是保密的
2.  计算`n=p×q`
    *   n用作公钥和私钥的模数(modules)，它的长度就是密钥长度。
    *   n作为公钥的一部分发布。如果大数分解成为可能，RSA算法将不再安全。
3.  计算`λ(n)`
    *   λ是Carmichael\\'s totient函数。 `λ(n) = lcm(λ(p), λ(q))`，因为p、q均为素数，所以`λ(p) = φ(p) = p − 1` 、 `λ(q) = φ(q) = q − 1`，从而`λ(n) = lcm(p − 1, q − 1)`。
    *   `lcm(a,b) = |ab|/gcd(a,b)`
    *   `λ(n)`是保密的
4.  选择一个整数e使得`1 < e < λ ( n )`且e和`λ(n)`互质
    *   通常选择216 + 1 = 65537，最小且最快的e是3，但是已经被证明在某些情况下是不安全的
    *   e作为公钥的一部分发布
5.  计算e对于`λ(n)`的模反元素d，满足`d⋅e ≡ 1 (mod λ(n))`
    *   d也就是密钥当中用来解密的那个数字，是私钥的一部分
    *   RSA原始论文中，直接使用欧拉函数`φ(n) = (p − 1)(q − 1`计算d

> In the original RSA paper, the Euler totient function φ(n) = (p − 1)(q − 1) is used instead of λ(n) for calculating the private exponent d. Since φ(n) is always divisible by λ(n) the algorithm works as well. That the Euler totient function can be used can also be seen as a consequence of Lagrange\\'s theorem applied to the multiplicative group of integers modulo pq. Thus any d satisfying d⋅e ≡ 1 (mod φ(n)) also satisfies d⋅e ≡ 1 (mod λ(n)). However, computing d modulo φ(n) will sometimes yield a result that is larger than necessary (i.e. d > λ(n)). Most of the implementations of RSA will accept exponents generated using either method (if they use the private exponent d at all, rather than using the optimized decryption method based on the Chinese remainder theorem described below), but some standards such as FIPS 186-4 may require that d < λ(n). Any oversized private exponents not meeting that criterion may always be reduced modulo λ(n) to obtain a smaller equivalent exponent. Since any common factors of (p − 1) and (q − 1) are present in the factorisation of n − 1 = pq − 1 = (p − 1)(q − 1) + (p − 1) + (q − 1), it is recommended that (p − 1) and (q − 1) have only very small common factors, if any besides the necessary 2. Note: The authors of the original RSA paper carry out the key generation by choosing d and then computing e as the modular multiplicative inverse of d modulo φ(n), whereas most current implementations of RSA, such as those following PKCS#1, do the reverse (choose e and compute d). Since the chosen key can be small whereas the computed key normally is not, the RSA paper\\'s algorithm optimizes decryption compared to encryption, while the modern algorithm optimizes encryption instead.

### 密钥分发

将n和e封装成公钥，分发公钥时只需保证可靠性，不需要保密性 ### RSA加密 对明文进行比特串分组，使得每个分组对应的十进制数小于n，然后依次对每个分组m做一次加密，所有分组的密文构成的序列就是原始消息的加密结果。对每个满足`0 ≤ m < n`的分组m的加密方法为：`m^e ≡ c (mod n)`，c即为本组需要传输的密文。 ### RSA解密 对于每个`0 ≤ c < n`的密文，`c^d ≡ m (mod n)`，m即为c经过解密后的明文。 ### 数字签名 将私钥d作为加密密钥对明文进行加密，这样可以得到仅有私钥拥有者可以加密，但是任何公钥拥有者都可以解密的消息，从而提供了数字签名。