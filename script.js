/**
 * Portal Kabupaten Bandung Barat — script.js
 * Vanilla ES6, no external dependencies.
 */

document.addEventListener('DOMContentLoaded', () => {

  const kecamatanData = {
    lembang: {
      nama: 'Kecamatan Lembang',
      alamat: 'Jl. Kayu Ambon, Kayuambon, Kec. Lembang, Kabupaten Bandung Barat',
      desa: [
        { nama: 'Cikole', kepalaDesa: 'Bpk. Asep Sudrajat', penduduk: 11840, laki: 5890, perempuan: 5950, kk: 3710, luas: 4.8, kepadatan: 2467, rtRw: '13/7', kodePos: '40391' },
        { nama: 'Cikahuripan', kepalaDesa: 'Bpk. Deni Suryana', penduduk: 9780, laki: 4890, perempuan: 4890, kk: 3050, luas: 4.2, kepadatan: 2329, rtRw: '12/6', kodePos: '40392' },
        { nama: 'Cibodas', kepalaDesa: 'Bpk. Budi Hartono', penduduk: 12400, laki: 6205, perempuan: 6195, kk: 3900, luas: 5.1, kepadatan: 2431, rtRw: '14/8', kodePos: '40391' },
        { nama: 'Kayuambon', kepalaDesa: 'Bpk. Raka Kusnadi', penduduk: 10950, laki: 5470, perempuan: 5480, kk: 3430, luas: 4.9, kepadatan: 2235, rtRw: '11/7', kodePos: '40391' },
        { nama: 'Lembang', kepalaDesa: 'Bpk. Ujang Suryana', penduduk: 14350, laki: 7150, perempuan: 7200, kk: 4450, luas: 6.3, kepadatan: 2278, rtRw: '15/8', kodePos: '40391' },
        { nama: 'Pagerwangi', kepalaDesa: 'Bpk. Yudi Permana', penduduk: 10220, laki: 5080, perempuan: 5140, kk: 3180, luas: 4.7, kepadatan: 2174, rtRw: '12/6', kodePos: '40391' },
        { nama: 'Sukaraja', kepalaDesa: 'Bpk. Irman Hermawan', penduduk: 9650, laki: 4825, perempuan: 4825, kk: 2980, luas: 4.1, kepadatan: 2354, rtRw: '10/5', kodePos: '40392' },
        { nama: 'Suntenjaya', kepalaDesa: 'Bpk. Agus Mulyana', penduduk: 9240, laki: 4620, perempuan: 4620, kk: 2870, luas: 3.9, kepadatan: 2369, rtRw: '11/5', kodePos: '40392' }
      ]
    },
    parongpong: {
      nama: 'Kecamatan Parongpong',
      alamat: 'Jl. Kolonel Masturi no.291, Cihanjuang Rahayu, Kecamatan Parongpong, Kabupaten Bandung Barat',
      desa: [
        { nama: 'Cihideung', kepalaDesa: 'Bpk. Ade Hidayat', penduduk: 9140, laki: 4580, perempuan: 4560, kk: 2830, luas: 3.7, kepadatan: 2470, rtRw: '10/6', kodePos: '40559' },
        { nama: 'Cihanjuang', kepalaDesa: 'Bpk. Asep Koswara', penduduk: 8570, laki: 4300, perempuan: 4270, kk: 2680, luas: 3.2, kepadatan: 2678, rtRw: '9/5', kodePos: '40559' },
        { nama: 'Cihanjuang Rahayu', kepalaDesa: 'Bpk. Yana Supriatna', penduduk: 12120, laki: 6080, perempuan: 6040, kk: 3870, luas: 4.5, kepadatan: 2693, rtRw: '14/8', kodePos: '40559' },
        { nama: 'Ciwaruga', kepalaDesa: 'Bpk. Samsul Ma’arif', penduduk: 10380, laki: 5180, perempuan: 5200, kk: 3360, luas: 4.1, kepadatan: 2532, rtRw: '12/7', kodePos: '40559' },
        { nama: 'Kutawaringin', kepalaDesa: 'Bpk. Sugeng Riyadi', penduduk: 8840, laki: 4430, perempuan: 4410, kk: 2710, luas: 3.5, kepadatan: 2526, rtRw: '10/6', kodePos: '40559' },
        { nama: 'Mekarwangi', kepalaDesa: 'Bpk. Agus Rahmat', penduduk: 9125, laki: 4565, perempuan: 4560, kk: 2790, luas: 2.9, kepadatan: 3147, rtRw: '9/5', kodePos: '40559' }
      ]
    },
    cisarua: {
      nama: 'Kecamatan Cisarua',
      alamat: 'Jalan Terusan Cisarua Padalarang No.10, Cisarua, Kab. Bandung Barat',
      desa: [
        { nama: 'Cisarua', kepalaDesa: 'Bpk. Taufik Hidayat', penduduk: 14560, laki: 7310, perempuan: 7250, kk: 4720, luas: 6.1, kepadatan: 2387, rtRw: '15/8', kodePos: '40551' },
        { nama: 'Barusari', kepalaDesa: 'Bpk. Roni Darmawan', penduduk: 8450, laki: 4230, perempuan: 4220, kk: 2600, luas: 3.8, kepadatan: 2224, rtRw: '10/6', kodePos: '40551' },
        { nama: 'Baturetno', kepalaDesa: 'Bpk. Kurniawan', penduduk: 9620, laki: 4815, perempuan: 4805, kk: 3000, luas: 4.2, kepadatan: 2290, rtRw: '11/7', kodePos: '40551' },
        { nama: 'Bunijaya', kepalaDesa: 'Bpk. Dedi Iskandar', penduduk: 10720, laki: 5350, perempuan: 5370, kk: 3320, luas: 4.6, kepadatan: 2330, rtRw: '12/6', kodePos: '40551' },
        { nama: 'Kopo', kepalaDesa: 'Bpk. Sandi Permana', penduduk: 8900, laki: 4450, perempuan: 4450, kk: 2790, luas: 3.9, kepadatan: 2282, rtRw: '9/5', kodePos: '40551' },
        { nama: 'Selacai', kepalaDesa: 'Bpk. Eko Wahyudi', penduduk: 8310, laki: 4160, perempuan: 4150, kk: 2460, luas: 3.5, kepadatan: 2374, rtRw: '9/5', kodePos: '40551' }
      ]
    },
    cikalongwetan: {
      nama: 'Kecamatan Cikalongwetan',
      alamat: 'Jl. Raya Cikalongwetan No. 506, Cikalong Wetan, Kabupaten Bandung Barat',
      desa: [
        { nama: 'Cikalong Wetan', kepalaDesa: 'Bpk. H. Deden', penduduk: 16840, laki: 8420, perempuan: 8420, kk: 5330, luas: 8.2, kepadatan: 2054, rtRw: '16/9', kodePos: '40556' },
        { nama: 'Cikampung', kepalaDesa: 'Bpk. Ujang Iskandar', penduduk: 9770, laki: 4900, perempuan: 4870, kk: 3085, luas: 4.7, kepadatan: 2077, rtRw: '11/6', kodePos: '40556' },
        { nama: 'Girimulya', kepalaDesa: 'Bpk. Edi Gunawan', penduduk: 10910, laki: 5480, perempuan: 5430, kk: 3410, luas: 5.3, kepadatan: 2059, rtRw: '12/7', kodePos: '40556' },
        { nama: 'Jatisari', kepalaDesa: 'Bpk. Ahmad Sopian', penduduk: 9150, laki: 4560, perempuan: 4590, kk: 2850, luas: 4.4, kepadatan: 2080, rtRw: '10/6', kodePos: '40556' },
        { nama: 'Mandalasari', kepalaDesa: 'Bpk. Tono Hermawan', penduduk: 10260, laki: 5110, perempuan: 5150, kk: 3210, luas: 5.0, kepadatan: 2052, rtRw: '12/7', kodePos: '40556' },
        { nama: 'Nagrak', kepalaDesa: 'Bpk. Syarif Hidayat', penduduk: 9810, laki: 4890, perempuan: 4920, kk: 3040, luas: 4.8, kepadatan: 2044, rtRw: '11/6', kodePos: '40556' }
      ]
    },
    cipeundeuy: {
      nama: 'Kecamatan Cipeundeuy',
      alamat: 'Jl. Raya Cipeundeuy No.513, Cipeundeuy, Kabupaten Bandung Barat',
      desa: [
        { nama: 'Cipeundeuy', kepalaDesa: 'Bpk. H. Andri', penduduk: 9860, laki: 4920, perempuan: 4940, kk: 3050, luas: 4.9, kepadatan: 2012, rtRw: '11/6', kodePos: '40565' },
        { nama: 'Cihuni', kepalaDesa: 'Bpk. Edi Suhardi', penduduk: 8940, laki: 4470, perempuan: 4470, kk: 2780, luas: 4.1, kepadatan: 2180, rtRw: '10/5', kodePos: '40565' },
        { nama: 'Karangnuggal', kepalaDesa: 'Bpk. H. Sutisna', penduduk: 8210, laki: 4080, perempuan: 4130, kk: 2470, luas: 3.7, kepadatan: 2219, rtRw: '9/5', kodePos: '40565' },
        { nama: 'Leuwi', kepalaDesa: 'Bpk. Asep Nurbani', penduduk: 7480, laki: 3720, perempuan: 3760, kk: 2210, luas: 3.3, kepadatan: 2267, rtRw: '8/4', kodePos: '40565' },
        { nama: 'Mekarjaya', kepalaDesa: 'Bpk. Cecep Hermawan', penduduk: 8730, laki: 4340, perempuan: 4390, kk: 2680, luas: 3.9, kepadatan: 2238, rtRw: '9/5', kodePos: '40565' },
        { nama: 'Rancamandala', kepalaDesa: 'Bpk. Jajang S', penduduk: 8190, laki: 4080, perempuan: 4110, kk: 2440, luas: 3.6, kepadatan: 2275, rtRw: '9/5', kodePos: '40565' }
      ]
    },
    ngamprah: {
      nama: 'Kecamatan Ngamprah',
      alamat: 'Komplek Pemda Kabupaten Bandung Barat Jl. Raya Padalarang-Cisarua Km.2 Ngamprah',
      desa: [
        { nama: 'Ngamprah', kepalaDesa: 'Bpk. H. Dicky', penduduk: 18440, laki: 9200, perempuan: 9240, kk: 5780, luas: 7.6, kepadatan: 2426, rtRw: '17/9', kodePos: '40552' },
        { nama: 'Cilame', kepalaDesa: 'Bpk. Hendra', penduduk: 13720, laki: 6850, perempuan: 6870, kk: 4280, luas: 5.5, kepadatan: 2495, rtRw: '14/8', kodePos: '40552' },
        { nama: 'Bojongkoneng', kepalaDesa: 'Bpk. Iwan', penduduk: 12680, laki: 6340, perempuan: 6340, kk: 3970, luas: 4.9, kepadatan: 2588, rtRw: '13/7', kodePos: '40552' },
        { nama: 'Gombong', kepalaDesa: 'Bpk. Syarifudin', penduduk: 10230, laki: 5130, perempuan: 5100, kk: 3190, luas: 4.2, kepadatan: 2436, rtRw: '12/6', kodePos: '40552' },
        { nama: 'Margajaya', kepalaDesa: 'Bpk. Deden', penduduk: 11820, laki: 5900, perempuan: 5920, kk: 3660, luas: 5.1, kepadatan: 2318, rtRw: '12/7', kodePos: '40552' },
        { nama: 'Sukaresmi', kepalaDesa: 'Bpk. A. Rafi', penduduk: 10990, laki: 5480, perempuan: 5510, kk: 3440, luas: 4.8, kepadatan: 2288, rtRw: '11/6', kodePos: '40552' }
      ]
    },
    cipatat: {
      nama: 'Kecamatan Cipatat',
      alamat: 'Jl. Raya Cipatat No.177, Cipatat, Kec. Cipatat, Kabupaten Bandung Barat',
      desa: [
        { nama: 'Cipatat', kepalaDesa: 'Bpk. H. M. Nasir', penduduk: 16550, laki: 8270, perempuan: 8280, kk: 5210, luas: 7.2, kepadatan: 2299, rtRw: '18/9', kodePos: '40554' },
        { nama: 'Cipongkor', kepalaDesa: 'Bpk. Deni', penduduk: 9820, laki: 4900, perempuan: 4920, kk: 3020, luas: 4.4, kepadatan: 2232, rtRw: '11/6', kodePos: '40554' },
        { nama: 'Kiarasari', kepalaDesa: 'Bpk. Edi', penduduk: 11140, laki: 5550, perempuan: 5590, kk: 3460, luas: 5.2, kepadatan: 2142, rtRw: '12/7', kodePos: '40554' },
        { nama: 'Mandalajati', kepalaDesa: 'Bpk. Saja', penduduk: 9080, laki: 4550, perempuan: 4530, kk: 2810, luas: 4.0, kepadatan: 2270, rtRw: '10/5', kodePos: '40554' },
        { nama: 'Nanggeleng', kepalaDesa: 'Bpk. Yusup', penduduk: 10360, laki: 5170, perempuan: 5190, kk: 3210, luas: 4.6, kepadatan: 2252, rtRw: '11/6', kodePos: '40554' },
        { nama: 'Raharja', kepalaDesa: 'Bpk. Wawan', penduduk: 9470, laki: 4730, perempuan: 4740, kk: 2940, luas: 4.3, kepadatan: 2202, rtRw: '10/6', kodePos: '40554' }
      ]
    },
    padalarang: {
      nama: 'Kecamatan Padalarang',
      alamat: 'Jl. Sudimampir hilir rt.01 rw.17 Padalarang, Bandung Barat, Jawa Barat 40553',
      desa: [
        { nama: 'Padalarang', kepalaDesa: 'Bpk. H. Mustopa', penduduk: 21780, laki: 10890, perempuan: 10890, kk: 6500, luas: 9.1, kepadatan: 2393, rtRw: '22/11', kodePos: '40553' },
        { nama: 'Cimanggu', kepalaDesa: 'Bpk. Ujang', penduduk: 12090, laki: 6020, perempuan: 6070, kk: 3830, luas: 5.8, kepadatan: 2084, rtRw: '13/8', kodePos: '40553' },
        { nama: 'Kertajaya', kepalaDesa: 'Bpk. Surya', penduduk: 14360, laki: 7180, perempuan: 7180, kk: 4510, luas: 6.2, kepadatan: 2316, rtRw: '16/8', kodePos: '40553' },
        { nama: 'Mekarsari', kepalaDesa: 'Bpk. Tedi', penduduk: 10230, laki: 5110, perempuan: 5120, kk: 3220, luas: 4.7, kepadatan: 2177, rtRw: '11/6', kodePos: '40553' },
        { nama: 'Sariwangi', kepalaDesa: 'Bpk. Eman', penduduk: 13720, laki: 6850, perempuan: 6870, kk: 4330, luas: 6.4, kepadatan: 2144, rtRw: '14/7', kodePos: '40553' },
        { nama: 'Wangunharja', kepalaDesa: 'Bpk. H. Soeparman', penduduk: 9160, laki: 4580, perempuan: 4580, kk: 2880, luas: 3.9, kepadatan: 2351, rtRw: '10/5', kodePos: '40553' }
      ]
    },
    batujajar: {
      nama: 'Kecamatan Batujajar',
      alamat: 'Jl. Raya Batujajar No.145 Desa Batujajar Timur',
      desa: [
        { nama: 'Batujajar Timur', kepalaDesa: 'Bpk. H. Andi', penduduk: 11920, laki: 5960, perempuan: 5960, kk: 3710, luas: 4.8, kepadatan: 2483, rtRw: '12/7', kodePos: '40561' },
        { nama: 'Batujajar Barat', kepalaDesa: 'Bpk. Maman', penduduk: 11360, laki: 5660, perempuan: 5700, kk: 3560, luas: 5.1, kepadatan: 2227, rtRw: '12/7', kodePos: '40561' },
        { nama: 'Cijulang', kepalaDesa: 'Bpk. Rina', penduduk: 9180, laki: 4590, perempuan: 4590, kk: 2870, luas: 3.6, kepadatan: 2550, rtRw: '10/5', kodePos: '40561' },
        { nama: 'Cintaasih', kepalaDesa: 'Bpk. Ogi', penduduk: 10340, laki: 5160, perempuan: 5180, kk: 3230, luas: 4.5, kepadatan: 2298, rtRw: '11/6', kodePos: '40561' },
        { nama: 'Mekarjaya', kepalaDesa: 'Bpk. Yadi', penduduk: 10780, laki: 5380, perempuan: 5400, kk: 3350, luas: 4.6, kepadatan: 2343, rtRw: '12/6', kodePos: '40561' },
        { nama: 'Pangauban', kepalaDesa: 'Bpk. Dadang', penduduk: 9210, laki: 4590, perempuan: 4620, kk: 2870, luas: 3.8, kepadatan: 2424, rtRw: '10/5', kodePos: '40561' }
      ]
    },
    cihampelas: {
      nama: 'Kecamatan Cihampelas',
      alamat: 'Jln. Raya Ciraden No.08, Kab. Bandung Barat',
      desa: [
        { nama: 'Cihampelas', kepalaDesa: 'Bpk. H. Agus', penduduk: 13640, laki: 6820, perempuan: 6820, kk: 4270, luas: 6.3, kepadatan: 2165, rtRw: '15/8', kodePos: '40562' },
        { nama: 'Cihanjawar', kepalaDesa: 'Bpk. Budi', penduduk: 9100, laki: 4550, perempuan: 4550, kk: 2820, luas: 4.1, kepadatan: 2219, rtRw: '9/5', kodePos: '40562' },
        { nama: 'Cisurupan', kepalaDesa: 'Bpk. Ujang', penduduk: 10420, laki: 5210, perempuan: 5210, kk: 3230, luas: 4.7, kepadatan: 2217, rtRw: '12/6', kodePos: '40562' },
        { nama: 'Mandalawangi', kepalaDesa: 'Bpk. Jajang', penduduk: 8900, laki: 4460, perempuan: 4440, kk: 2760, luas: 4.0, kepadatan: 2225, rtRw: '10/5', kodePos: '40562' },
        { nama: 'Nagrak', kepalaDesa: 'Bpk. Asep', penduduk: 9720, laki: 4860, perempuan: 4860, kk: 3010, luas: 4.4, kepadatan: 2209, rtRw: '11/6', kodePos: '40562' },
        { nama: 'Sukarame', kepalaDesa: 'Bpk. Dadi', penduduk: 8680, laki: 4340, perempuan: 4340, kk: 2690, luas: 3.8, kepadatan: 2284, rtRw: '9/5', kodePos: '40562' }
      ]
    },
    cililin: {
      nama: 'Kecamatan Cililin',
      alamat: 'Jl. Raya Cililin No.1 Desa Cililin, Kab. Bandung Barat',
      desa: [
        { nama: 'Cililin', kepalaDesa: 'Bpk. H. Suwarno', penduduk: 13820, laki: 6890, perempuan: 6930, kk: 4300, luas: 6.4, kepadatan: 2159, rtRw: '15/8', kodePos: '40562' },
        { nama: 'Banjarsari', kepalaDesa: 'Bpk. Ade', penduduk: 10420, laki: 5200, perempuan: 5220, kk: 3230, luas: 4.9, kepadatan: 2127, rtRw: '12/6', kodePos: '40562' },
        { nama: 'Cikadang', kepalaDesa: 'Bpk. M. Aji', penduduk: 9160, laki: 4570, perempuan: 4590, kk: 2840, luas: 4.3, kepadatan: 2130, rtRw: '10/5', kodePos: '40562' },
        { nama: 'Cisomang', kepalaDesa: 'Bpk. Fajar', penduduk: 9790, laki: 4900, perempuan: 4890, kk: 3070, luas: 4.8, kepadatan: 2035, rtRw: '11/6', kodePos: '40562' },
        { nama: 'Karang', kepalaDesa: 'Bpk. Dede', penduduk: 8440, laki: 4210, perempuan: 4230, kk: 2630, luas: 4.1, kepadatan: 2059, rtRw: '9/5', kodePos: '40562' },
        { nama: 'Rancamanyar', kepalaDesa: 'Bpk. Eko', penduduk: 10140, laki: 5060, perempuan: 5080, kk: 3150, luas: 4.7, kepadatan: 2157, rtRw: '11/6', kodePos: '40562' }
      ]
    },
    cipongkor: {
      nama: 'Kecamatan Cipongkor',
      alamat: 'Jl. PLTA Saguling No. 1 Sarinagen, Cipongkor',
      desa: [
        { nama: 'Cipongkor', kepalaDesa: 'Bpk. H. Yamin', penduduk: 11120, laki: 5540, perempuan: 5580, kk: 3470, luas: 5.5, kepadatan: 2022, rtRw: '12/7', kodePos: '40567' },
        { nama: 'Buniasih', kepalaDesa: 'Bpk. Huda', penduduk: 8060, laki: 4020, perempuan: 4040, kk: 2490, luas: 4.2, kepadatan: 1919, rtRw: '9/5', kodePos: '40567' },
        { nama: 'Cijambu', kepalaDesa: 'Bpk. Tarmizi', penduduk: 8420, laki: 4210, perempuan: 4210, kk: 2610, luas: 4.4, kepadatan: 1914, rtRw: '9/5', kodePos: '40567' },
        { nama: 'Cipada', kepalaDesa: 'Bpk. Aji', penduduk: 9250, laki: 4620, perempuan: 4630, kk: 2860, luas: 4.8, kepadatan: 1927, rtRw: '10/6', kodePos: '40567' },
        { nama: 'Sarinagen', kepalaDesa: 'Bpk. Sule', penduduk: 9740, laki: 4870, perempuan: 4870, kk: 3010, luas: 5.0, kepadatan: 1948, rtRw: '10/6', kodePos: '40567' },
        { nama: 'Tugumukti', kepalaDesa: 'Bpk. Gani', penduduk: 8650, laki: 4320, perempuan: 4330, kk: 2690, luas: 4.3, kepadatan: 2012, rtRw: '9/5', kodePos: '40567' }
      ]
    },
    rongga: {
      nama: 'Kecamatan Rongga',
      alamat: 'Jl. Lebaksaat, Cibedug, Rongga, Bojongsalam, Kec. Rongga, Kabupaten Bandung Barat, Jawa Barat 40556',
      desa: [
        { nama: 'Rongga', kepalaDesa: 'Bpk. H. Deni', penduduk: 8310, laki: 4150, perempuan: 4160, kk: 2550, luas: 4.2, kepadatan: 1979, rtRw: '9/5', kodePos: '40556' },
        { nama: 'Bojongsalam', kepalaDesa: 'Bpk. Ilyas', penduduk: 9520, laki: 4760, perempuan: 4760, kk: 2950, luas: 4.8, kepadatan: 1983, rtRw: '10/5', kodePos: '40556' },
        { nama: 'Cibedug', kepalaDesa: 'Bpk. Yudi', penduduk: 10020, laki: 5010, perempuan: 5010, kk: 3110, luas: 5.2, kepadatan: 1927, rtRw: '11/6', kodePos: '40556' },
        { nama: 'Karyamukti', kepalaDesa: 'Bpk. Suyitno', penduduk: 8650, laki: 4320, perempuan: 4330, kk: 2690, luas: 4.6, kepadatan: 1880, rtRw: '9/5', kodePos: '40556' },
        { nama: 'Mekarmulya', kepalaDesa: 'Bpk. Heri', penduduk: 8920, laki: 4470, perempuan: 4450, kk: 2790, luas: 4.7, kepadatan: 1898, rtRw: '9/5', kodePos: '40556' },
        { nama: 'Parakanmuncang', kepalaDesa: 'Bpk. Sudirman', penduduk: 7780, laki: 3900, perempuan: 3880, kk: 2390, luas: 4.1, kepadatan: 1898, rtRw: '8/4', kodePos: '40556' }
      ]
    },
    sindangkerta: {
      nama: 'Kecamatan Sindangkerta',
      alamat: '2C53+95G, Cintakarya, Sindangkerta, Bandung Barat',
      desa: [
        { nama: 'Sindangkerta', kepalaDesa: 'Bpk. H. Rohmat', penduduk: 12850, laki: 6430, perempuan: 6420, kk: 3980, luas: 5.9, kepadatan: 2178, rtRw: '14/8', kodePos: '40564' },
        { nama: 'Cintakarya', kepalaDesa: 'Bpk. Arif', penduduk: 9810, laki: 4910, perempuan: 4900, kk: 3040, luas: 4.6, kepadatan: 2135, rtRw: '11/6', kodePos: '40564' },
        { nama: 'Karyasari', kepalaDesa: 'Bpk. Dadan', penduduk: 10720, laki: 5360, perempuan: 5360, kk: 3320, luas: 5.1, kepadatan: 2102, rtRw: '12/7', kodePos: '40564' },
        { nama: 'Mekarjaya', kepalaDesa: 'Bpk. Soni', penduduk: 9510, laki: 4740, perempuan: 4770, kk: 2910, luas: 4.2, kepadatan: 2264, rtRw: '10/6', kodePos: '40564' },
        { nama: 'Rancapanggung', kepalaDesa: 'Bpk. Taryono', penduduk: 8950, laki: 4470, perempuan: 4480, kk: 2780, luas: 4.0, kepadatan: 2238, rtRw: '9/5', kodePos: '40564' },
        { nama: 'Wangunsari', kepalaDesa: 'Bpk. Yayan', penduduk: 10230, laki: 5120, perempuan: 5110, kk: 3180, luas: 4.7, kepadatan: 2177, rtRw: '11/6', kodePos: '40564' }
      ]
    },
    gununghalu: {
      nama: 'Kecamatan Gununghalu',
      alamat: 'Jl. Raya Pasanggrahan No. 1, Sirnajaya, Gununghalu, Sirnajaya, Bandung Barat',
      desa: [
        { nama: 'Gununghalu', kepalaDesa: 'Bpk. H. Suryana', penduduk: 12680, laki: 6340, perempuan: 6340, kk: 3960, luas: 6.1, kepadatan: 2079, rtRw: '13/7', kodePos: '40566' },
        { nama: 'Cikahuripan', kepalaDesa: 'Bpk. Nurdin', penduduk: 7440, laki: 3720, perempuan: 3720, kk: 2340, luas: 3.5, kepadatan: 2126, rtRw: '8/4', kodePos: '40566' },
        { nama: 'Cisirung', kepalaDesa: 'Bpk. Iman', penduduk: 8270, laki: 4140, perempuan: 4130, kk: 2570, luas: 4.1, kepadatan: 2017, rtRw: '9/5', kodePos: '40566' },
        { nama: 'Mekarlaksana', kepalaDesa: 'Bpk. Maman', penduduk: 7880, laki: 3940, perempuan: 3940, kk: 2450, luas: 3.8, kepadatan: 2074, rtRw: '8/4', kodePos: '40566' },
        { nama: 'Sirnajaya', kepalaDesa: 'Bpk. Agus', penduduk: 9740, laki: 4870, perempuan: 4870, kk: 3050, luas: 4.7, kepadatan: 2072, rtRw: '10/6', kodePos: '40566' },
        { nama: 'Sukajaya', kepalaDesa: 'Bpk. Dendi', penduduk: 9150, laki: 4570, perempuan: 4580, kk: 2850, luas: 4.4, kepadatan: 2080, rtRw: '10/5', kodePos: '40566' }
      ]
    },
    saguling: {
      nama: 'Kecamatan Saguling',
      alamat: 'Jl. Raya Saguling Km. 19',
      desa: [
        { nama: 'Saguling', kepalaDesa: 'Bpk. H. Totok', penduduk: 12190, laki: 6100, perempuan: 6090, kk: 3780, luas: 5.7, kepadatan: 2139, rtRw: '13/7', kodePos: '40563' },
        { nama: 'Bojongmanggu', kepalaDesa: 'Bpk. Yana', penduduk: 10420, laki: 5200, perempuan: 5220, kk: 3230, luas: 4.9, kepadatan: 2127, rtRw: '11/6', kodePos: '40563' },
        { nama: 'Cilangkap', kepalaDesa: 'Bpk. H. Asep', penduduk: 9780, laki: 4890, perempuan: 4890, kk: 3040, luas: 4.7, kepadatan: 2081, rtRw: '10/6', kodePos: '40563' },
        { nama: 'Karyamekar', kepalaDesa: 'Bpk. Ayi', penduduk: 9020, laki: 4510, perempuan: 4510, kk: 2800, luas: 4.3, kepadatan: 2098, rtRw: '10/5', kodePos: '40563' },
        { nama: 'Mekarwangi', kepalaDesa: 'Bpk. Sugih', penduduk: 9430, laki: 4700, perempuan: 4730, kk: 2930, luas: 4.4, kepadatan: 2143, rtRw: '10/6', kodePos: '40563' },
        { nama: 'Rancabali', kepalaDesa: 'Bpk. Yusup', penduduk: 8450, laki: 4220, perempuan: 4230, kk: 2620, luas: 4.1, kepadatan: 2061, rtRw: '9/5', kodePos: '40563' }
      ]
    }
  };

  const normalizeKecamatanKey = (value) => {
    return String(value || '')
      .toLowerCase()
      .trim()
      .replace(/[^a-z0-9]+/g, '-')
      .replace(/^-+|-+$/g, '');
  };

  const desaImagePool = [
    'https://images.unsplash.com/photo-1501785888041-af3ef285b470?auto=format&fit=crop&w=1200&q=80',
    'https://images.unsplash.com/photo-1470770841072-f978cf4d019e?auto=format&fit=crop&w=1200&q=80',
    'https://images.unsplash.com/photo-1465146344425-f00d5f5c8f07?auto=format&fit=crop&w=1200&q=80',
    'https://images.unsplash.com/photo-1500530855697-b586d89ba3ee?auto=format&fit=crop&w=1200&q=80',
    'https://images.unsplash.com/photo-1506744038136-46273834b3fb?auto=format&fit=crop&w=1200&q=80',
    'https://images.unsplash.com/photo-1501854140801-50d01698950b?auto=format&fit=crop&w=1200&q=80'
  ];

  const getDesaImage = (desaName, districtName) => {
    const seed = `${districtName}-${desaName}`.toLowerCase().split('').reduce((acc, char) => acc + char.charCodeAt(0), 0);
    return desaImagePool[seed % desaImagePool.length];
  };

  const defaultPotensi = [
    { icon: '🌾', title: 'Pertanian', desc: 'Potensi pertanian dan lahan produktif mendukung kesejahteraan masyarakat desa.' },
    { icon: '🏞️', title: 'Pariwisata', desc: 'Kawasan alam dan budaya desa menjadi daya tarik wisata lokal dan domestik.' },
    { icon: '🐄', title: 'Peternakan', desc: 'Kegiatan peternakan dan usaha ternak menjadi pendukung ekonomi rumah tangga.' },
    { icon: '🏪', title: 'UMKM', desc: 'Usaha mikro dan produk lokal menjadi motor penggerak perekonomian desa.' }
  ];

  const getVillagePotensi = (desa, district) => {
    if (Array.isArray(desa.potensi) && desa.potensi.length) return desa.potensi;

    const districtName = district.nama.replace('Kecamatan ', '');
    const base = [
      { icon: '🌾', title: 'Pertanian', desc: `Potensi pertanian di ${desa.nama} menjadi sumber utama penghidupan masyarakat di wilayah ${districtName}.` },
      { icon: '🏞️', title: 'Pariwisata', desc: `Potensi alam dan budaya di ${desa.nama} mendukung pengembangan wisata lokal yang berkelanjutan.` },
      { icon: '🐄', title: 'Peternakan', desc: `Kegiatan peternakan dan usaha ternak di ${desa.nama} menambah pendapatan masyarakat.` },
      { icon: '🏪', title: 'UMKM', desc: `Produk lokal dan usaha mikro di ${desa.nama} menjadi pendorong ekonomi desa.` }
    ];

    return base;
  };

  const getVillageGallery = (desa, district) => {
    if (Array.isArray(desa.galeri) && desa.galeri.length) return desa.galeri;

    const districtName = district.nama.replace('Kecamatan ', '');
    const base = [
      `https://images.unsplash.com/photo-1500534623283-312aade485b7?auto=format&fit=crop&w=900&q=80`,
      `https://images.unsplash.com/photo-1501854140801-50d01698950b?auto=format&fit=crop&w=900&q=80`,
      `https://images.unsplash.com/photo-1464822759023-fed622ff2c3b?auto=format&fit=crop&w=900&q=80`,
      `https://images.unsplash.com/photo-1470770841072-f978cf4d019e?auto=format&fit=crop&w=900&q=80`
    ];

    return base.map((img, index) => {
      const seed = `${districtName}-${desa.nama}-${index}`.toLowerCase();
      const hash = Array.from(seed).reduce((acc, ch) => acc + ch.charCodeAt(0), 0);
      return base[(hash + index) % base.length];
    }).slice(0, 4);
  };

  const enrichKecamatanData = () => {
    Object.values(kecamatanData).forEach((district) => {
      if (!Array.isArray(district.desa)) return;

      district.desa = district.desa.map((desa, index) => ({
        ...desa,
        mapQuery: desa.mapQuery || `${desa.nama}, ${district.nama}, Kabupaten Bandung Barat`,
        potensi: getVillagePotensi(desa, district),
        galeri: getVillageGallery(desa, district),
        keterangan: desa.keterangan || `${desa.nama} adalah salah satu desa di wilayah ${district.nama} yang memiliki potensi pertanian, pariwisata, dan ekonomi lokal yang berkembang.`
      }));
    });
  };

  enrichKecamatanData();

  const renderDesaDetail = (desa, district) => {
    const panel = document.getElementById('desaDetailPanel');
    if (!panel) return;

    const mapSrc = `https://www.google.com/maps?q=${encodeURIComponent(desa.mapQuery || `${desa.nama}, ${district.nama}, Kabupaten Bandung Barat`)}&output=embed`;
    const potensiMarkup = (desa.potensi || defaultPotensi).map((item) => `
      <div class="desa-potensi-card">
        <div class="desa-potensi-icon">${item.icon}</div>
        <h4>${item.title}</h4>
        <p>${item.desc}</p>
      </div>
    `).join('');

    const galleryMarkup = (desa.galeri || getVillageGallery(desa, district)).slice(0, 4).map((img) => `
      <div class="desa-gallery-item">
        <img src="${img}" alt="Galeri ${desa.nama}" loading="lazy" />
      </div>
    `).join('');

    panel.hidden = false;
    panel.innerHTML = `
      <div class="desa-detail-top">
        <div class="crumb">Beranda › Desa › ${district.nama}</div>
        <button class="close-detail" type="button" aria-label="Tutup detail desa">Tutup</button>
      </div>
      <div class="desa-detail-layout">
        <div class="desa-detail-figure">
          <img src="${getDesaImage(desa.nama, district.nama)}" alt="${desa.nama}" loading="lazy" />
        </div>
        <div class="desa-detail-copy">
          <div>
            <h3>${desa.nama}</h3>
            <p class="subtext">${desa.keterangan || `Desa yang terletak di wilayah ${district.nama}, dengan potensi pertanian, pariwisata, dan aktivitas sosial ekonomi yang berkembang di sekitar kawasan perkotaan dan pedesaan.`}</p>
          </div>
          <div class="desa-detail-meta">
            <div class="item"><span>Nama Desa</span><strong>${desa.nama}</strong></div>
            <div class="item"><span>Kecamatan</span><strong>${district.nama.replace('Kecamatan ', '')}</strong></div>
            <div class="item"><span>Kepala Desa</span><strong>${desa.kepalaDesa}</strong></div>
            <div class="item"><span>Kode Pos</span><strong>${desa.kodePos}</strong></div>
          </div>
          <div class="desa-detail-stats">
            <div class="desa-stat-box"><span>Penduduk</span><strong>${desa.penduduk.toLocaleString('id-ID')}</strong></div>
            <div class="desa-stat-box"><span>Laki-laki</span><strong>${desa.laki.toLocaleString('id-ID')}</strong></div>
            <div class="desa-stat-box"><span>Perempuan</span><strong>${desa.perempuan.toLocaleString('id-ID')}</strong></div>
            <div class="desa-stat-box"><span>KK</span><strong>${desa.kk.toLocaleString('id-ID')}</strong></div>
          </div>
          <div class="desa-map-box">
            <iframe class="desa-map-frame" src="${mapSrc}" loading="lazy" allowfullscreen referrerpolicy="no-referrer-when-downgrade"></iframe>
            <div class="map-label">Peta wilayah ${desa.nama}</div>
          </div>
        </div>
      </div>

      <div class="desa-potensi-wrap">
        <div class="desa-section-header">Potensi Desa</div>
        <div class="desa-potensi-grid">
          ${potensiMarkup}
        </div>
      </div>

      <div class="desa-gallery-wrap">
        <div class="desa-section-header">Galeri Desa</div>
        <div class="desa-gallery-grid">
          ${galleryMarkup}
        </div>
      </div>
    `;

    panel.querySelector('.close-detail').addEventListener('click', () => {
      panel.hidden = true;
      document.querySelectorAll('.desa-card-item').forEach((card) => {
        card.classList.remove('is-open');
        const btn = card.querySelector('.desa-detail-btn');
        if (btn) {
          btn.textContent = 'Detail';
          btn.setAttribute('aria-expanded', 'false');
        }
      });
    });
  };

  const sum = (items, key) => items.reduce((total, item) => total + Number(item[key] || 0), 0);

  const renderKecamatanDetail = () => {
    const page = document.getElementById('kecamatanDetailPage');
    if (!page) return;

    const params = new URLSearchParams(window.location.search);
    const kecamatanKey = normalizeKecamatanKey(params.get('kecamatan') || 'lembang');
    const district = kecamatanData[kecamatanKey] || kecamatanData.lembang;
    const desaList = district.desa || [];
    const totalPenduduk = sum(desaList, 'penduduk');
    const totalLaki = sum(desaList, 'laki');
    const totalPerempuan = sum(desaList, 'perempuan');
    const totalKk = sum(desaList, 'kk');
    const totalLuas = desaList.reduce((acc, item) => acc + Number(item.luas || 0), 0);

    const detailTitleBreadcrumb = document.getElementById('detailTitleBreadcrumb');
    const detailTitleMain = document.getElementById('detailTitleMain');

    if (detailTitleBreadcrumb) detailTitleBreadcrumb.textContent = district.nama;
    if (detailTitleMain) detailTitleMain.textContent = district.nama;
    document.getElementById('detailSubtitle').textContent = `${desaList.length} desa/kelurahan • Data penduduk dan profil wilayah`;
    document.getElementById('detailAlamat').textContent = district.alamat;
    document.getElementById('detailPenduduk').textContent = totalPenduduk.toLocaleString('id-ID');
    document.getElementById('detailLaki').textContent = totalLaki.toLocaleString('id-ID');
    document.getElementById('detailPerempuan').textContent = totalPerempuan.toLocaleString('id-ID');
    document.getElementById('detailKK').textContent = totalKk.toLocaleString('id-ID');
    document.getElementById('detailLuas').textContent = `${totalLuas.toFixed(1).replace('.', ',')} km²`;
    document.getElementById('detailKepadatan').textContent = `${Math.round(totalPenduduk / totalLuas).toLocaleString('id-ID')} jiwa/km²`;

    const desaGrid = document.getElementById('desaCardGrid');
    if (desaGrid) {
      desaGrid.innerHTML = desaList.map((desa, index) => `
        <div class="desa-card-item" data-index="${index}">
          <div class="desa-card-header">
            <span class="desa-card-no">${index + 1}</span>
            <div class="desa-card-title">
              <h3>${desa.nama}</h3>
              <p class="desa-card-kepala">${desa.kepalaDesa}</p>
            </div>
          </div>
          <div class="desa-card-body">
            <div class="desa-card-stat">
              <span class="label">PENDUDUK</span>
              <strong>${desa.penduduk.toLocaleString('id-ID')}</strong>
            </div>
            <div class="desa-card-stat">
              <span class="label">KK</span>
              <strong>${desa.kk.toLocaleString('id-ID')}</strong>
            </div>
          </div>
          <button class="desa-detail-btn" type="button" aria-expanded="false">Detail</button>
        </div>
      `).join('');

      desaGrid.querySelectorAll('.desa-detail-btn').forEach((button) => {
        button.addEventListener('click', () => {
          const card = button.closest('.desa-card-item');
          const index = Number(card.dataset.index || 0);
          const isOpen = card.classList.toggle('is-open');
          button.setAttribute('aria-expanded', String(isOpen));
          button.textContent = isOpen ? 'Tutup' : 'Detail';

          document.querySelectorAll('.desa-card-item').forEach((otherCard) => {
            if (otherCard !== card) {
              otherCard.classList.remove('is-open');
              const otherButton = otherCard.querySelector('.desa-detail-btn');
              if (otherButton) {
                otherButton.textContent = 'Detail';
                otherButton.setAttribute('aria-expanded', 'false');
              }
            }
          });

          if (isOpen) {
            renderDesaDetail(desaList[index], district);
          } else {
            const panel = document.getElementById('desaDetailPanel');
            if (panel) panel.hidden = true;
          }
        });
      });
    }

    const navList = document.getElementById('kecamatanNavList');
    if (navList) {
      navList.innerHTML = Object.entries(kecamatanData).map(([key, item]) => `
        <a href="kecamatan-detail.html?kecamatan=${key}" class="${key === kecamatanKey ? 'active' : ''}">${item.nama}</a>
      `).join('');
    }
  };

  const initKecamatanDetailLinks = () => {
    const districtNames = {
      'kecamatan-lembang': 'lembang',
      'kecamatan-parongpong': 'parongpong',
      'kecamatan-cisarua': 'cisarua',
      'kecamatan-cikalongwetan': 'cikalongwetan',
      'kecamatan-cipeundeuy': 'cipeundeuy',
      'kecamatan-ngamprah': 'ngamprah',
      'kecamatan-cipatat': 'cipatat',
      'kecamatan-padalarang': 'padalarang',
      'kecamatan-batujajar': 'batujajar',
      'kecamatan-cihampelas': 'cihampelas',
      'kecamatan-cililin': 'cililin',
      'kecamatan-cipongkor': 'cipongkor',
      'kecamatan-rongga': 'rongga',
      'kecamatan-sindangkerta': 'sindangkerta',
      'kecamatan-gununghalu': 'gununghalu',
      'kecamatan-saguling': 'saguling'
    };

    document.querySelectorAll('.detail-button').forEach((button) => {
      const explicitHref = button.getAttribute('data-kecamatan');
      const href = explicitHref || button.getAttribute('href');
      const districtKey = explicitHref ? normalizeKecamatanKey(explicitHref) : normalizeKecamatanKey(href || '');
      const mappedKey = districtNames[districtKey] || districtKey;

      if (mappedKey === 'lembang') {
        button.setAttribute('href', 'lembang.html');
        button.setAttribute('aria-label', 'Detail Kecamatan Lembang');
        return;
      }

      if (mappedKey && kecamatanData[mappedKey]) {
        button.setAttribute('href', `kecamatan-detail.html?kecamatan=${mappedKey}`);
        button.setAttribute('aria-label', `Detail ${kecamatanData[mappedKey].nama}`);
      }
    });
  };

  // ─────────────────────────────────────────────────────────────
  // 1. MOBILE SIDEBAR TOGGLE
  // ─────────────────────────────────────────────────────────────

  const menuToggle = document.getElementById('menuToggle');
  const sidebar    = document.getElementById('sidebar');
  const shell      = document.querySelector('.shell');

  if (menuToggle && sidebar) {
    // Open / close sidebar when the hamburger button is clicked
    menuToggle.addEventListener('click', (e) => {
      e.stopPropagation();
      const isOpen = sidebar.classList.toggle('open');
      menuToggle.setAttribute('aria-label', isOpen ? 'Tutup menu' : 'Buka menu');
      menuToggle.innerHTML = isOpen ? '&times;' : '&#9776;';
    });

    // Close sidebar when clicking anywhere outside of it (on the shell overlay)
    document.addEventListener('click', (e) => {
      if (
        sidebar.classList.contains('open') &&
        !sidebar.contains(e.target) &&
        e.target !== menuToggle
      ) {
        sidebar.classList.remove('open');
        menuToggle.setAttribute('aria-label', 'Buka menu');
        menuToggle.innerHTML = '&#9776;';
      }
    });
  }


  // ─────────────────────────────────────────────────────────────
  // 2. SIDEBAR SUBMENU ACCORDION
  // ─────────────────────────────────────────────────────────────

  const currentPath = window.location.pathname.split('/').pop() || 'index.html';
  const submenuTriggers = document.querySelectorAll('.has-submenu > .nav-parent');

  submenuTriggers.forEach((trigger) => {
    const item = trigger.closest('.has-submenu');
    if (!item) return;

    const targetHref = trigger.getAttribute('href');
    const linkPage = targetHref ? targetHref.split('/').pop() : '';
    const isCurrentPage = !!(linkPage && linkPage !== '#' && linkPage === currentPath);

    trigger.addEventListener('click', (e) => {
      const shouldToggle = !targetHref || targetHref === '#' || isCurrentPage;

      if (shouldToggle) {
        e.preventDefault();

        const isAlreadyOpen = item.classList.contains('submenu-open');
        const siblingSubmenus = item.parentElement.querySelectorAll(':scope > .has-submenu');

        // Close only sibling submenus at the same nesting level.
        siblingSubmenus.forEach((other) => {
          if (other !== item) {
            other.classList.remove('submenu-open');
          }
        });

        // Toggle the clicked item.
        item.classList.toggle('submenu-open', !isAlreadyOpen);
      }
    });
  });


  // ─────────────────────────────────────────────────────────────
  // 3. TOPNAV DROPDOWN
  // ─────────────────────────────────────────────────────────────

  const topnavItems = document.querySelectorAll('.topnav-item');

  topnavItems.forEach((item) => {
    const dropdown = item.querySelector('.tn-dropdown');
    const trigger  = item.querySelector('a.has-tn-dropdown');

    if (!dropdown || !trigger) return; // No dropdown — skip

    // Toggle this item's dropdown on click
    trigger.addEventListener('click', (e) => {
      e.preventDefault(); // Don't follow href="#" for parent links

      const isAlreadyOpen = item.classList.contains('tn-open');

      // Close all other open topnav dropdowns (exclusive)
      topnavItems.forEach((other) => {
        if (other !== item) {
          other.classList.remove('tn-open');
        }
      });

      // Toggle the clicked item
      item.classList.toggle('tn-open', !isAlreadyOpen);
    });
  });

  // Close all topnav dropdowns when clicking anywhere outside the topnav
  document.addEventListener('click', (e) => {
    const topnav = document.querySelector('.topnav');
    if (topnav && !topnav.contains(e.target)) {
      topnavItems.forEach((item) => item.classList.remove('tn-open'));
    }
  });

  // Close topnav dropdowns when pressing Escape
  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') {
      topnavItems.forEach((item) => item.classList.remove('tn-open'));
    }
  });


  // ─────────────────────────────────────────────────────────────
  // 4. ACTIVE NAV HIGHLIGHT
  // ─────────────────────────────────────────────────────────────

  /**
   * Match the current page URL against sidebar and topnav link hrefs.
   * Add 'active' class to the matching link and its parent container.
   * Falls back gracefully to the first item if no match is found.
   */

  // — Sidebar links —
  const sidenavLinks = document.querySelectorAll('nav.sidenav a');
  sidenavLinks.forEach((link) => {
    link.classList.remove('active');
    const linkPage = link.getAttribute('href').split('/').pop();
    if (linkPage && linkPage !== '#' && linkPage === currentPath) {
      link.classList.add('active');

      // Open the full ancestor chain for the active page so nested routes
      // like Rumah Sakit / Puskesmas keep their parent branches expanded.
      let currentMenuItem = link.closest('.has-submenu');
      while (currentMenuItem) {
        const siblingMenus = currentMenuItem.parentElement.querySelectorAll(':scope > .has-submenu');
        siblingMenus.forEach((other) => {
          if (other !== currentMenuItem) {
            other.classList.remove('submenu-open');
          }
        });
        currentMenuItem.classList.add('submenu-open');
        currentMenuItem = currentMenuItem.parentElement.closest('.has-submenu');
      }
    }
  });

  // — Topnav items —
  // Remove any hard-coded 'active' from the HTML first
  topnavItems.forEach((item) => {
    item.classList.remove('active');
    const links = item.querySelectorAll('a');
    links.forEach((link) => {
      const linkPage = link.getAttribute('href').split('/').pop();
      if (linkPage && linkPage !== '#' && linkPage === currentPath) {
        item.classList.add('active');
      }
    });
  });

  // If we're on the root/index, mark the first topnav item (Beranda) active
  if (
    currentPath === '' ||
    currentPath === 'index.html' ||
    currentPath === '/'
  ) {
    // Only set active on Beranda if nothing else matched
    const anyActive = document.querySelector('.topnav-item.active');
    if (!anyActive && topnavItems.length > 0) {
      topnavItems[0].classList.add('active');
    }
  }


  // ─────────────────────────────────────────────────────────────
  // 5. DIR-ROW INTERACTION
  // ─────────────────────────────────────────────────────────────

  /**
   * The hover arrow animation on .dir-row is handled entirely by CSS
   * (transform: translateX(4px) on :hover). No JS needed for that.
   *
   * A click ripple or navigation behaviour can be wired here if needed
   * in a future iteration, e.g.:
   *
   *   document.querySelectorAll('.dir-row').forEach((row) => {
   *     row.addEventListener('click', () => { window.location.href = row.dataset.href; });
   *   });
   */

  // ─────────────────────────────────────────────────────────────
  // 6. BERITA TERKINI SLIDER (scrollable feature-card carousel)
  // ─────────────────────────────────────────────────────────────

  document.querySelectorAll('.news-featured').forEach((section) => {
    const slider = section.querySelector('.feature-slider');
    const prevBtn = section.querySelector('.slider-prev');
    const nextBtn = section.querySelector('.slider-next');
    if (!slider) return;

    const scrollByCard = (direction) => {
      slider.scrollBy({ left: slider.clientWidth * direction, behavior: 'smooth' });
    };

    if (prevBtn) prevBtn.addEventListener('click', () => scrollByCard(-1));
    if (nextBtn) nextBtn.addEventListener('click', () => scrollByCard(1));
  });

  // ─────────────────────────────────────────────────────────────
  // 7. KECAMATAN DETAIL PAGE / DETAIL BUTTONS
  // ─────────────────────────────────────────────────────────────

  initKecamatanDetailLinks();
  renderKecamatanDetail();

}); // end DOMContentLoaded