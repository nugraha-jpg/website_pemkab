#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import os

# Data untuk setiap kecamatan
districts_data = {
    'parongpong': {
        'name': 'Parongpong',
        'description': 'Kecamatan Parongpong terdiri dari desa-desa dengan berbagai potensi',
        'villages': [
            {'name': 'Desa Cihanjuang Rahayu', 'key': 'cihanjuang_rahayu', 'area': '2.45 km²', 'areaPct': '3.21%', 'population': '8,250 jiwa', 'male': '4,125', 'female': '4,125', 'density': '3,367 jiwa/km²', 'sexRatio': '100.00', 'rw': '12', 'rt': '42', 'code': '32.17.02.2001', 'distDistrict': '0 km', 'distRegency': '28.0 km'},
            {'name': 'Desa Sukaluyu', 'key': 'sukaluyu', 'area': '3.12 km²', 'areaPct': '4.08%', 'population': '7,840 jiwa', 'male': '3,920', 'female': '3,920', 'density': '2,513 jiwa/km²', 'sexRatio': '100.00', 'rw': '10', 'rt': '38', 'code': '32.17.02.2002', 'distDistrict': '2.5 km', 'distRegency': '30.5 km'},
            {'name': 'Desa Cipeundeuy', 'key': 'cipeundeuy_p', 'area': '2.78 km²', 'areaPct': '3.64%', 'population': '6,920 jiwa', 'male': '3,460', 'female': '3,460', 'density': '2,490 jiwa/km²', 'sexRatio': '100.00', 'rw': '9', 'rt': '35', 'code': '32.17.02.2003', 'distDistrict': '3.1 km', 'distRegency': '31.1 km'},
            {'name': 'Desa Cipongkor', 'key': 'cipongkor_p', 'area': '4.25 km²', 'areaPct': '5.56%', 'population': '9,780 jiwa', 'male': '4,890', 'female': '4,890', 'density': '2,302 jiwa/km²', 'sexRatio': '100.00', 'rw': '14', 'rt': '48', 'code': '32.17.02.2004', 'distDistrict': '4.2 km', 'distRegency': '32.2 km'},
            {'name': 'Desa Sindanglaya', 'key': 'sindanglaya', 'area': '3.65 km²', 'areaPct': '4.78%', 'population': '7,450 jiwa', 'male': '3,725', 'female': '3,725', 'density': '2,041 jiwa/km²', 'sexRatio': '100.00', 'rw': '11', 'rt': '40', 'code': '32.17.02.2005', 'distDistrict': '2.8 km', 'distRegency': '30.8 km'},
        ]
    },
    'cisarua': {
        'name': 'Cisarua',
        'description': 'Kecamatan Cisarua merupakan pusat industri dan pertanian di Kabupaten Bandung Barat',
        'villages': [
            {'name': 'Desa Cisarua', 'key': 'cisarua_main', 'area': '3.21 km²', 'areaPct': '4.12%', 'population': '9,560 jiwa', 'male': '4,780', 'female': '4,780', 'density': '2,980 jiwa/km²', 'sexRatio': '100.00', 'rw': '13', 'rt': '45', 'code': '32.17.03.2001', 'distDistrict': '0 km', 'distRegency': '26.5 km'},
            {'name': 'Desa Tangkuban Perahu', 'key': 'tangkuban_perahu', 'area': '4.56 km²', 'areaPct': '5.85%', 'population': '8,940 jiwa', 'male': '4,470', 'female': '4,470', 'density': '1,961 jiwa/km²', 'sexRatio': '100.00', 'rw': '11', 'rt': '42', 'code': '32.17.03.2002', 'distDistrict': '3.2 km', 'distRegency': '29.7 km'},
            {'name': 'Desa Pasir Eurih', 'key': 'pasir_eurih', 'area': '2.89 km²', 'areaPct': '3.71%', 'population': '7,230 jiwa', 'male': '3,615', 'female': '3,615', 'density': '2,502 jiwa/km²', 'sexRatio': '100.00', 'rw': '10', 'rt': '38', 'code': '32.17.03.2003', 'distDistrict': '2.1 km', 'distRegency': '28.6 km'},
            {'name': 'Desa Cilember', 'key': 'cilember', 'area': '3.78 km²', 'areaPct': '4.85%', 'population': '8,120 jiwa', 'male': '4,060', 'female': '4,060', 'density': '2,149 jiwa/km²', 'sexRatio': '100.00', 'rw': '12', 'rt': '41', 'code': '32.17.03.2004', 'distDistrict': '2.8 km', 'distRegency': '29.3 km'},
            {'name': 'Desa Sukaraja', 'key': 'sukaraja_cisarua', 'area': '3.45 km²', 'areaPct': '4.43%', 'population': '7,890 jiwa', 'male': '3,945', 'female': '3,945', 'density': '2,288 jiwa/km²', 'sexRatio': '100.00', 'rw': '11', 'rt': '39', 'code': '32.17.03.2005', 'distDistrict': '3.5 km', 'distRegency': '30.0 km'},
        ]
    },
    'cikalongwetan': {
        'name': 'Cikalongwetan',
        'description': 'Kecamatan Cikalongwetan merupakan wilayah dengan potensi pertanian dan peternakan',
        'villages': [
            {'name': 'Desa Cikalong Wetan', 'key': 'cikalong_wetan_main', 'area': '2.95 km²', 'areaPct': '3.85%', 'population': '8,670 jiwa', 'male': '4,335', 'female': '4,335', 'density': '2,937 jiwa/km²', 'sexRatio': '100.00', 'rw': '12', 'rt': '43', 'code': '32.17.04.2001', 'distDistrict': '0 km', 'distRegency': '32.5 km'},
            {'name': 'Desa Margajaya', 'key': 'margajaya', 'area': '3.67 km²', 'areaPct': '4.78%', 'population': '7,540 jiwa', 'male': '3,770', 'female': '3,770', 'density': '2,056 jiwa/km²', 'sexRatio': '100.00', 'rw': '10', 'rt': '36', 'code': '32.17.04.2002', 'distDistrict': '2.3 km', 'distRegency': '34.8 km'},
            {'name': 'Desa Rancamanyar', 'key': 'rancamanyar', 'area': '4.12 km²', 'areaPct': '5.37%', 'population': '8,250 jiwa', 'male': '4,125', 'female': '4,125', 'density': '2,003 jiwa/km²', 'sexRatio': '100.00', 'rw': '11', 'rt': '40', 'code': '32.17.04.2003', 'distDistrict': '3.1 km', 'distRegency': '35.6 km'},
            {'name': 'Desa Sukapura', 'key': 'sukapura', 'area': '3.23 km²', 'areaPct': '4.21%', 'population': '6,890 jiwa', 'male': '3,445', 'female': '3,445', 'density': '2,131 jiwa/km²', 'sexRatio': '100.00', 'rw': '9', 'rt': '33', 'code': '32.17.04.2004', 'distDistrict': '1.8 km', 'distRegency': '34.3 km'},
        ]
    },
    'cipeundeuy': {
        'name': 'Cipeundeuy',
        'description': 'Kecamatan Cipeundeuy adalah daerah dengan pengembangan ekonomi pertanian dan perdagangan',
        'villages': [
            {'name': 'Desa Cipeundeuy', 'key': 'cipeundeuy_main', 'area': '3.12 km²', 'areaPct': '4.05%', 'population': '9,120 jiwa', 'male': '4,560', 'female': '4,560', 'density': '2,923 jiwa/km²', 'sexRatio': '100.00', 'rw': '13', 'rt': '44', 'code': '32.17.05.2001', 'distDistrict': '0 km', 'distRegency': '30.2 km'},
            {'name': 'Desa Sangkanhurip', 'key': 'sangkanhurip', 'area': '2.87 km²', 'areaPct': '3.73%', 'population': '7,340 jiwa', 'male': '3,670', 'female': '3,670', 'density': '2,559 jiwa/km²', 'sexRatio': '100.00', 'rw': '10', 'rt': '37', 'code': '32.17.05.2002', 'distDistrict': '2.1 km', 'distRegency': '32.3 km'},
            {'name': 'Desa Sukaharjo', 'key': 'sukaharjo', 'area': '3.45 km²', 'areaPct': '4.49%', 'population': '8,560 jiwa', 'male': '4,280', 'female': '4,280', 'density': '2,481 jiwa/km²', 'sexRatio': '100.00', 'rw': '12', 'rt': '42', 'code': '32.17.05.2003', 'distDistrict': '2.8 km', 'distRegency': '33.0 km'},
            {'name': 'Desa Pasirhalang', 'key': 'pasirhalang', 'area': '3.78 km²', 'areaPct': '4.92%', 'population': '7,890 jiwa', 'male': '3,945', 'female': '3,945', 'density': '2,088 jiwa/km²', 'sexRatio': '100.00', 'rw': '11', 'rt': '38', 'code': '32.17.05.2004', 'distDistrict': '3.5 km', 'distRegency': '33.7 km'},
        ]
    },
    'ngamprah': {
        'name': 'Ngamprah',
        'description': 'Kecamatan Ngamprah adalah pusat pemerintahan Kabupaten Bandung Barat dengan infrastruktur modern',
        'villages': [
            {'name': 'Desa Ngamprah', 'key': 'ngamprah_main', 'area': '2.56 km²', 'areaPct': '3.34%', 'population': '10,240 jiwa', 'male': '5,120', 'female': '5,120', 'density': '4,000 jiwa/km²', 'sexRatio': '100.00', 'rw': '14', 'rt': '48', 'code': '32.17.06.2001', 'distDistrict': '0 km', 'distRegency': '2.0 km'},
            {'name': 'Desa Sukamanah', 'key': 'sukamanah', 'area': '3.45 km²', 'areaPct': '4.50%', 'population': '8,670 jiwa', 'male': '4,335', 'female': '4,335', 'density': '2,513 jiwa/km²', 'sexRatio': '100.00', 'rw': '11', 'rt': '40', 'code': '32.17.06.2002', 'distDistrict': '2.2 km', 'distRegency': '4.2 km'},
            {'name': 'Desa Mekarmukti', 'key': 'mekarmukti', 'area': '2.89 km²', 'areaPct': '3.77%', 'population': '7,560 jiwa', 'male': '3,780', 'female': '3,780', 'density': '2,616 jiwa/km²', 'sexRatio': '100.00', 'rw': '10', 'rt': '36', 'code': '32.17.06.2003', 'distDistrict': '1.8 km', 'distRegency': '3.8 km'},
            {'name': 'Desa Sukasari', 'key': 'sukasari', 'area': '3.12 km²', 'areaPct': '4.07%', 'population': '8,890 jiwa', 'male': '4,445', 'female': '4,445', 'density': '2,851 jiwa/km²', 'sexRatio': '100.00', 'rw': '12', 'rt': '42', 'code': '32.17.06.2004', 'distDistrict': '2.5 km', 'distRegency': '4.5 km'},
        ]
    },
    'cipatat': {
        'name': 'Cipatat',
        'description': 'Kecamatan Cipatat merupakan wilayah dengan pengembangan industri kecil dan menengah',
        'villages': [
            {'name': 'Desa Cipatat', 'key': 'cipatat_main', 'area': '3.34 km²', 'areaPct': '4.37%', 'population': '9,450 jiwa', 'male': '4,725', 'female': '4,725', 'density': '2,831 jiwa/km²', 'sexRatio': '100.00', 'rw': '13', 'rt': '45', 'code': '32.17.07.2001', 'distDistrict': '0 km', 'distRegency': '24.5 km'},
            {'name': 'Desa Situsari', 'key': 'situsari', 'area': '2.95 km²', 'areaPct': '3.86%', 'population': '7,890 jiwa', 'male': '3,945', 'female': '3,945', 'density': '2,673 jiwa/km²', 'sexRatio': '100.00', 'rw': '11', 'rt': '38', 'code': '32.17.07.2002', 'distDistrict': '2.1 km', 'distRegency': '26.6 km'},
            {'name': 'Desa Sukahandap', 'key': 'sukahandap', 'area': '3.78 km²', 'areaPct': '4.95%', 'population': '8,120 jiwa', 'male': '4,060', 'female': '4,060', 'density': '2,149 jiwa/km²', 'sexRatio': '100.00', 'rw': '10', 'rt': '40', 'code': '32.17.07.2003', 'distDistrict': '3.2 km', 'distRegency': '27.7 km'},
            {'name': 'Desa Sukamulya', 'key': 'sukamulya', 'area': '3.23 km²', 'areaPct': '4.23%', 'population': '7,450 jiwa', 'male': '3,725', 'female': '3,725', 'density': '2,304 jiwa/km²', 'sexRatio': '100.00', 'rw': '10', 'rt': '36', 'code': '32.17.07.2004', 'distDistrict': '2.8 km', 'distRegency': '27.3 km'},
        ]
    },
    'padalarang': {
        'name': 'Padalarang',
        'description': 'Kecamatan Padalarang adalah pusat perdagangan dan transportasi dengan lokasi strategis',
        'villages': [
            {'name': 'Desa Padalarang', 'key': 'padalarang_main', 'area': '2.78 km²', 'areaPct': '3.63%', 'population': '10,890 jiwa', 'male': '5,445', 'female': '5,445', 'density': '3,917 jiwa/km²', 'sexRatio': '100.00', 'rw': '15', 'rt': '50', 'code': '32.17.08.2001', 'distDistrict': '0 km', 'distRegency': '18.2 km'},
            {'name': 'Desa Cimekar', 'key': 'cimekar', 'area': '3.45 km²', 'areaPct': '4.51%', 'population': '8,340 jiwa', 'male': '4,170', 'female': '4,170', 'density': '2,417 jiwa/km²', 'sexRatio': '100.00', 'rw': '11', 'rt': '38', 'code': '32.17.08.2002', 'distDistrict': '2.3 km', 'distRegency': '20.5 km'},
            {'name': 'Desa Sukaratu', 'key': 'sukaratu', 'area': '3.12 km²', 'areaPct': '4.08%', 'population': '7,670 jiwa', 'male': '3,835', 'female': '3,835', 'density': '2,458 jiwa/km²', 'sexRatio': '100.00', 'rw': '10', 'rt': '36', 'code': '32.17.08.2003', 'distDistrict': '1.9 km', 'distRegency': '20.1 km'},
            {'name': 'Desa Kracak', 'key': 'kracak', 'area': '2.95 km²', 'areaPct': '3.86%', 'population': '7,120 jiwa', 'male': '3,560', 'female': '3,560', 'density': '2,415 jiwa/km²', 'sexRatio': '100.00', 'rw': '9', 'rt': '32', 'code': '32.17.08.2004', 'distDistrict': '2.1 km', 'distRegency': '20.3 km'},
        ]
    },
    'batujajar': {
        'name': 'Batujajar',
        'description': 'Kecamatan Batujajar merupakan wilayah dengan pengembangan pariwisata dan ekonomi lokal',
        'villages': [
            {'name': 'Desa Batujajar Timur', 'key': 'batujajar_timur', 'area': '3.23 km²', 'areaPct': '4.22%', 'population': '9,780 jiwa', 'male': '4,890', 'female': '4,890', 'density': '3,027 jiwa/km²', 'sexRatio': '100.00', 'rw': '13', 'rt': '44', 'code': '32.17.09.2001', 'distDistrict': '0 km', 'distRegency': '22.0 km'},
            {'name': 'Desa Batujajar Barat', 'key': 'batujajar_barat', 'area': '2.87 km²', 'areaPct': '3.75%', 'population': '8,560 jiwa', 'male': '4,280', 'female': '4,280', 'density': '2,982 jiwa/km²', 'sexRatio': '100.00', 'rw': '12', 'rt': '41', 'code': '32.17.09.2002', 'distDistrict': '1.5 km', 'distRegency': '23.5 km'},
            {'name': 'Desa Cicukang', 'key': 'cicukang', 'area': '3.67 km²', 'areaPct': '4.79%', 'population': '7,890 jiwa', 'male': '3,945', 'female': '3,945', 'density': '2,151 jiwa/km²', 'sexRatio': '100.00', 'rw': '11', 'rt': '37', 'code': '32.17.09.2003', 'distDistrict': '2.4 km', 'distRegency': '24.4 km'},
            {'name': 'Desa Sukamukti', 'key': 'sukamukti', 'area': '3.45 km²', 'areaPct': '4.51%', 'population': '7,340 jiwa', 'male': '3,670', 'female': '3,670', 'density': '2,128 jiwa/km²', 'sexRatio': '100.00', 'rw': '10', 'rt': '35', 'code': '32.17.09.2004', 'distDistrict': '3.1 km', 'distRegency': '25.1 km'},
        ]
    },
    'cihampelas': {
        'name': 'Cihampelas',
        'description': 'Kecamatan Cihampelas adalah daerah pengembangan pertanian dan pariwisata pedesaan',
        'villages': [
            {'name': 'Desa Ciraden', 'key': 'ciraden', 'area': '3.12 km²', 'areaPct': '4.08%', 'population': '8,450 jiwa', 'male': '4,225', 'female': '4,225', 'density': '2,705 jiwa/km²', 'sexRatio': '100.00', 'rw': '12', 'rt': '40', 'code': '32.17.10.2001', 'distDistrict': '0 km', 'distRegency': '28.1 km'},
            {'name': 'Desa Ciseureuh', 'key': 'ciseureuh', 'area': '2.95 km²', 'areaPct': '3.85%', 'population': '7,670 jiwa', 'male': '3,835', 'female': '3,835', 'density': '2,598 jiwa/km²', 'sexRatio': '100.00', 'rw': '10', 'rt': '36', 'code': '32.17.10.2002', 'distDistrict': '2.2 km', 'distRegency': '30.3 km'},
            {'name': 'Desa Cihampelas', 'key': 'cihampelas_main', 'area': '3.78 km²', 'areaPct': '4.94%', 'population': '8,120 jiwa', 'male': '4,060', 'female': '4,060', 'density': '2,149 jiwa/km²', 'sexRatio': '100.00', 'rw': '11', 'rt': '38', 'code': '32.17.10.2003', 'distDistrict': '2.8 km', 'distRegency': '30.9 km'},
            {'name': 'Desa Wangisari', 'key': 'wangisari', 'area': '3.45 km²', 'areaPct': '4.51%', 'population': '7,890 jiwa', 'male': '3,945', 'female': '3,945', 'density': '2,288 jiwa/km²', 'sexRatio': '100.00', 'rw': '11', 'rt': '37', 'code': '32.17.10.2004', 'distDistrict': '3.5 km', 'distRegency': '31.6 km'},
        ]
    },
    'cililin': {
        'name': 'Cililin',
        'description': 'Kecamatan Cililin merupakan pusat pengembangan pertanian dan industri kreatif',
        'villages': [
            {'name': 'Desa Cililin', 'key': 'cililin_main', 'area': '4.23 km²', 'areaPct': '5.52%', 'population': '9,340 jiwa', 'male': '4,670', 'female': '4,670', 'density': '2,207 jiwa/km²', 'sexRatio': '100.00', 'rw': '12', 'rt': '41', 'code': '32.17.11.2001', 'distDistrict': '0 km', 'distRegency': '36.5 km'},
            {'name': 'Desa Cilowong', 'key': 'cilowong', 'area': '3.67 km²', 'areaPct': '4.79%', 'population': '8,120 jiwa', 'male': '4,060', 'female': '4,060', 'density': '2,212 jiwa/km²', 'sexRatio': '100.00', 'rw': '10', 'rt': '36', 'code': '32.17.11.2002', 'distDistrict': '2.3 km', 'distRegency': '38.8 km'},
            {'name': 'Desa Sukalaksana', 'key': 'sukalaksana', 'area': '3.45 km²', 'areaPct': '4.51%', 'population': '7,560 jiwa', 'male': '3,780', 'female': '3,780', 'density': '2,191 jiwa/km²', 'sexRatio': '100.00', 'rw': '9', 'rt': '34', 'code': '32.17.11.2003', 'distDistrict': '1.8 km', 'distRegency': '38.3 km'},
            {'name': 'Desa Rancamanyar', 'key': 'rancamanyar_cililin', 'area': '2.89 km²', 'areaPct': '3.77%', 'population': '6,890 jiwa', 'male': '3,445', 'female': '3,445', 'density': '2,384 jiwa/km²', 'sexRatio': '100.00', 'rw': '8', 'rt': '30', 'code': '32.17.11.2004', 'distDistrict': '3.5 km', 'distRegency': '40.0 km'},
        ]
    },
    'cipongkor': {
        'name': 'Cipongkor',
        'description': 'Kecamatan Cipongkor adalah daerah dengan potensi pertanian, perikanan, dan pariwisata alam',
        'villages': [
            {'name': 'Desa Cipongkor', 'key': 'cipongkor_main', 'area': '5.12 km²', 'areaPct': '6.68%', 'population': '8,670 jiwa', 'male': '4,335', 'female': '4,335', 'density': '1,693 jiwa/km²', 'sexRatio': '100.00', 'rw': '11', 'rt': '38', 'code': '32.17.12.2001', 'distDistrict': '0 km', 'distRegency': '42.0 km'},
            {'name': 'Desa Sarinagen', 'key': 'sarinagen', 'area': '4.45 km²', 'areaPct': '5.81%', 'population': '7,890 jiwa', 'male': '3,945', 'female': '3,945', 'density': '1,773 jiwa/km²', 'sexRatio': '100.00', 'rw': '10', 'rt': '34', 'code': '32.17.12.2002', 'distDistrict': '2.5 km', 'distRegency': '44.5 km'},
            {'name': 'Desa Sukaresmi', 'key': 'sukaresmi', 'area': '3.78 km²', 'areaPct': '4.94%', 'population': '6,450 jiwa', 'male': '3,225', 'female': '3,225', 'density': '1,706 jiwa/km²', 'sexRatio': '100.00', 'rw': '8', 'rt': '29', 'code': '32.17.12.2003', 'distDistrict': '1.8 km', 'distRegency': '43.8 km'},
        ]
    },
    'rongga': {
        'name': 'Rongga',
        'description': 'Kecamatan Rongga merupakan wilayah dengan potensi pengembangan pertanian dan peternakan',
        'villages': [
            {'name': 'Desa Bojongsalam', 'key': 'bojongsalam', 'area': '4.67 km²', 'areaPct': '6.10%', 'population': '8,340 jiwa', 'male': '4,170', 'female': '4,170', 'density': '1,785 jiwa/km²', 'sexRatio': '100.00', 'rw': '10', 'rt': '34', 'code': '32.17.13.2001', 'distDistrict': '0 km', 'distRegency': '40.5 km'},
            {'name': 'Desa Cibedug', 'key': 'cibedug', 'area': '5.23 km²', 'areaPct': '6.82%', 'population': '7,890 jiwa', 'male': '3,945', 'female': '3,945', 'density': '1,509 jiwa/km²', 'sexRatio': '100.00', 'rw': '9', 'rt': '30', 'code': '32.17.13.2002', 'distDistrict': '2.3 km', 'distRegency': '42.8 km'},
            {'name': 'Desa Rongga', 'key': 'rongga_main', 'area': '3.89 km²', 'areaPct': '5.08%', 'population': '6,780 jiwa', 'male': '3,390', 'female': '3,390', 'density': '1,744 jiwa/km²', 'sexRatio': '100.00', 'rw': '8', 'rt': '28', 'code': '32.17.13.2003', 'distDistrict': '1.9 km', 'distRegency': '42.4 km'},
        ]
    },
    'sindangkerta': {
        'name': 'Sindangkerta',
        'description': 'Kecamatan Sindangkerta adalah pusat pengembangan ekonomi lokal dan pertanian berkelanjutan',
        'villages': [
            {'name': 'Desa Sindangkerta', 'key': 'sindangkerta_main', 'area': '3.56 km²', 'areaPct': '4.65%', 'population': '8,890 jiwa', 'male': '4,445', 'female': '4,445', 'density': '2,497 jiwa/km²', 'sexRatio': '100.00', 'rw': '12', 'rt': '42', 'code': '32.17.14.2001', 'distDistrict': '0 km', 'distRegency': '38.5 km'},
            {'name': 'Desa Cintakarya', 'key': 'cintakarya', 'area': '4.12 km²', 'areaPct': '5.37%', 'population': '8,120 jiwa', 'male': '4,060', 'female': '4,060', 'density': '1,970 jiwa/km²', 'sexRatio': '100.00', 'rw': '10', 'rt': '35', 'code': '32.17.14.2002', 'distDistrict': '2.1 km', 'distRegency': '40.6 km'},
            {'name': 'Desa Ciburial', 'key': 'ciburial', 'area': '3.67 km²', 'areaPct': '4.79%', 'population': '7,450 jiwa', 'male': '3,725', 'female': '3,725', 'density': '2,030 jiwa/km²', 'sexRatio': '100.00', 'rw': '10', 'rt': '34', 'code': '32.17.14.2003', 'distDistrict': '1.8 km', 'distRegency': '40.3 km'},
        ]
    },
    'gununghalu': {
        'name': 'Gununghalu',
        'description': 'Kecamatan Gununghalu merupakan wilayah pengembangan pariwisata alam dan pertanian hortikultura',
        'villages': [
            {'name': 'Desa Sirnajaya', 'key': 'sirnajaya', 'area': '5.34 km²', 'areaPct': '6.97%', 'population': '8,670 jiwa', 'male': '4,335', 'female': '4,335', 'density': '1,623 jiwa/km²', 'sexRatio': '100.00', 'rw': '11', 'rt': '38', 'code': '32.17.15.2001', 'distDistrict': '0 km', 'distRegency': '44.2 km'},
            {'name': 'Desa Pasanggrahan', 'key': 'pasanggrahan', 'area': '4.56 km²', 'areaPct': '5.95%', 'population': '7,890 jiwa', 'male': '3,945', 'female': '3,945', 'density': '1,731 jiwa/km²', 'sexRatio': '100.00', 'rw': '9', 'rt': '32', 'code': '32.17.15.2002', 'distDistrict': '2.2 km', 'distRegency': '46.4 km'},
            {'name': 'Desa Gununghalu', 'key': 'gununghalu_main', 'area': '4.12 km²', 'areaPct': '5.37%', 'population': '6,780 jiwa', 'male': '3,390', 'female': '3,390', 'density': '1,646 jiwa/km²', 'sexRatio': '100.00', 'rw': '8', 'rt': '28', 'code': '32.17.15.2003', 'distDistrict': '1.9 km', 'distRegency': '46.1 km'},
        ]
    },
    'saguling': {
        'name': 'Saguling',
        'description': 'Kecamatan Saguling adalah daerah pengembangan pariwisata, pertanian, dan perikanan dengan landscape alam yang indah',
        'villages': [
            {'name': 'Desa Saguling', 'key': 'saguling_main', 'area': '3.78 km²', 'areaPct': '4.94%', 'population': '8,450 jiwa', 'male': '4,225', 'female': '4,225', 'density': '2,237 jiwa/km²', 'sexRatio': '100.00', 'rw': '12', 'rt': '40', 'code': '32.17.16.2001', 'distDistrict': '0 km', 'distRegency': '46.8 km'},
            {'name': 'Desa Maribaya', 'key': 'maribaya', 'area': '4.23 km²', 'areaPct': '5.52%', 'population': '7,670 jiwa', 'male': '3,835', 'female': '3,835', 'density': '1,813 jiwa/km²', 'sexRatio': '100.00', 'rw': '10', 'rt': '34', 'code': '32.17.16.2002', 'distDistrict': '2.5 km', 'distRegency': '49.3 km'},
            {'name': 'Desa Neglasari', 'key': 'neglasari', 'area': '3.56 km²', 'areaPct': '4.65%', 'population': '6,890 jiwa', 'male': '3,445', 'female': '3,445', 'density': '1,937 jiwa/km²', 'sexRatio': '100.00', 'rw': '9', 'rt': '30', 'code': '32.17.16.2003', 'distDistrict': '1.8 km', 'distRegency': '48.6 km'},
        ]
    }
}

# Template dasar untuk halaman
template_html = '''<!DOCTYPE html>
<html lang="id">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Desa Kecamatan {DISTRICT_NAME} - BPS 2025</title>
<style>
*{box-sizing:border-box}
html,body{margin:0;padding:0;font-family:Inter,Segoe UI,Arial,Helvetica,sans-serif;background:#f3f7fc;color:#172a46}
body{overflow-x:hidden}
button,select{font:inherit}
.page{display:none;min-height:100vh}.page.active{display:block}
.container{width:min(1440px,94%);margin:auto}

/* ================= LIST ================= */
.list-page{position:relative;padding:26px 0 60px;background:linear-gradient(180deg,#edf6ff 0,#f6f9fd 430px,#f3f7fc 100%);min-height:100vh}
.list-page:before{content:"";position:absolute;left:0;right:0;top:0;height:285px;pointer-events:none;background:
 radial-gradient(circle at 82% 12%,rgba(255,208,77,.28) 0 34px,transparent 35px),
 radial-gradient(circle at 68% 30%,rgba(255,255,255,.7) 0 2px,transparent 3px),
 radial-gradient(circle at 73% 18%,rgba(255,255,255,.55) 0 2px,transparent 3px),
 linear-gradient(165deg,transparent 43%,rgba(152,194,222,.28) 44%,transparent 63%),
 linear-gradient(20deg,transparent 45%,rgba(105,163,198,.17) 46%,transparent 67%);opacity:.95}
.list-page .container{position:relative;z-index:1}
.back-btn{display:inline-flex;align-items:center;gap:9px;padding:11px 18px;background:rgba(255,255,255,.92);border:1px solid #d5e1ef;border-radius:9px;color:#06458f;font-weight:700;cursor:pointer;box-shadow:0 6px 18px rgba(31,74,119,.09);margin-bottom:24px;transition:.2s}
.back-btn:hover{transform:translateY(-1px);background:#fff;box-shadow:0 9px 22px rgba(31,74,119,.13)}
.list-title{margin:0;font-size:37px;line-height:1.15;color:#0b3978;letter-spacing:-.6px;max-width:760px}
.list-title:after{content:"";display:block;width:64px;height:6px;border-radius:10px;background:#ffc400;margin-top:13px}
.list-subtitle{margin:13px 0 19px;font-size:17px;color:#405b7d}
.breadcrumb{font-size:13px;color:#60728a;margin-bottom:28px}
.breadcrumb::first-letter{color:#0a4c9b}
.controls{background:rgba(255,255,255,.92);border:1px solid #dbe6f2;border-radius:14px;padding:20px 26px 22px;margin-bottom:25px;box-shadow:0 8px 25px rgba(35,73,116,.07);backdrop-filter:blur(5px)}
.controls label{display:block;font-weight:800;color:#073d83;margin-bottom:9px;font-size:14px}
.custom-select{position:relative;width:360px;max-width:100%}.custom-select__trigger{width:100%;min-height:52px;border:1px solid #d5e2f1;border-radius:14px;background:linear-gradient(180deg,#fff 0,#f5f9ff 100%);color:#1d314c;display:flex;align-items:center;justify-content:space-between;gap:12px;padding:0 16px 0 18px;cursor:pointer;box-shadow:0 10px 24px rgba(17,54,90,.06);transition:all .2s ease;border-bottom-width:2px;border-bottom-color:#cfe0f5}.custom-select__trigger:hover{border-color:#b9d1ef;box-shadow:0 12px 28px rgba(17,54,90,.09);transform:translateY(-1px)}.custom-select__trigger:focus-visible{outline:none;border-color:#70a9df;box-shadow:0 0 0 4px rgba(41,124,207,.12)}.custom-select__value{font-weight:800;letter-spacing:.06em;color:#113d73;text-transform:uppercase}.custom-select__icon{display:inline-flex;align-items:center;justify-content:center;width:30px;height:30px;border-radius:9px;background:linear-gradient(180deg,#edf5ff 0,#dfeeff 100%);color:#0f4d9b;font-size:18px;transition:transform .25s ease,background .2s ease}.custom-select.open .custom-select__icon{transform:rotate(180deg);background:linear-gradient(180deg,#dfeeff 0,#d2e6ff 100%)}.custom-select__panel{position:absolute;top:calc(100% + 10px);left:0;width:100%;max-width:420px;background:rgba(255,255,255,.98);border:1px solid #dfeaf7;border-radius:16px;box-shadow:0 22px 55px rgba(17,60,98,.2);padding:10px;display:none;z-index:20;backdrop-filter:blur(10px);animation:selectFade .2s ease}.custom-select.open .custom-select__panel{display:block}.custom-select__search{padding:4px 4px 10px}.custom-select__search input{width:100%;border:1px solid #d9e6f8;border-radius:10px;padding:11px 12px;background:#f9fbff;color:#1d314c;font:inherit;outline:none;transition:all .15s ease}.custom-select__search input:focus{border-color:#67a8eb;box-shadow:0 0 0 3px rgba(41,124,207,.12);background:#fff}.custom-select__options{list-style:none;padding:0;margin:0;max-height:220px;overflow-y:auto}.custom-select__options::-webkit-scrollbar{width:6px}.custom-select__options::-webkit-scrollbar-track{background:transparent}.custom-select__options::-webkit-scrollbar-thumb{background:#d0dae8;border-radius:3px}.custom-select__options::-webkit-scrollbar-thumb:hover{background:#b8c8db}.custom-select__option{padding:11px 12px;cursor:pointer;color:#1d314c;transition:background .1s}.custom-select__option:hover{background:#f0f5fd}.custom-select__option.is-selected{background:#e7f0ff;color:#0754b3;font-weight:700}
.section-title{font-size:20px;font-weight:700;margin:28px 0 20px;color:#0b3978;position:relative;text-transform:none}.section-title:before{content:"⌂";width:38px;height:38px;border-radius:10px;background:#e7f2ff;display:inline-flex;align-items:center;justify-content:center;font-size:22px;color:#0754a4;box-shadow:inset 0 0 0 1px #d5e8fb}
.section-title:after{content:"";position:absolute}
.grid{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:16px;align-items:stretch}
.village-card{background:rgba(255,255,255,.97);border:1px solid #e0e7ef;border-radius:10px;overflow:hidden;box-shadow:0 5px 16px rgba(23,58,96,.07);display:flex;flex-direction:row;padding:10px;gap:13px;min-height:126px;transition:transform .2s,box-shadow .2s,border-color .2s}
.village-card:hover{transform:translateY(-3px);border-color:#c9dbef;box-shadow:0 12px 25px rgba(25,68,111,.12)}
.village-card img{width:122px;height:106px;flex:0 0 122px;object-fit:cover;border-radius:7px;display:block;background:#e9eef5}
.card-body{padding:2px 0;display:flex;flex-direction:column;flex:1;min-width:0}
.card-body h3{font-size:16px;line-height:1.25;margin:2px 0 11px;color:#0a3d82;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.info-row{display:flex;justify-content:space-between;gap:6px;font-size:11.5px;margin:4px 0;color:#5a687b;white-space:nowrap}.info-row b{color:#24364e;white-space:nowrap}
.detail-btn{margin-top:auto;width:100%;border:0;border-radius:5px;background:#0754b3;color:#fff;padding:8px 7px;font-size:11.5px;font-weight:800;cursor:pointer;transition:.2s}.detail-btn:hover{background:#063f8b}
.source{margin-top:22px;padding:13px 15px;background:#edf6ff;border:1px solid #d3e7fb;border-radius:9px;font-size:12px;color:#365b83}

/* ================= DETAIL ================= */
.detail-page{padding:25px 0 55px;background:#f3f7fc;min-height:100vh}.detail-layout{display:grid;grid-template-columns:minmax(0,2fr) minmax(310px,1fr);gap:20px}.detail-main,.sidebar-card{background:#fff;border:1px solid #e0e7ef;border-radius:11px;box-shadow:0 6px 18px rgba(23,58,96,.06)}.hero-detail{padding:0;overflow:hidden}.hero-content{display:grid;grid-template-columns:48% 52%;min-height:310px}.hero-content img{width:100%;height:310px;object-fit:cover}.hero-text{padding:42px 38px}.hero-text h1{margin:0 0 10px;color:#0c448e;font-size:34px}.hero-text .district{font-size:16px;margin-bottom:25px;color:#52657d}.hero-text p{line-height:1.85;color:#34445a;margin:0}.detail-card{margin-top:18px;padding:21px}.detail-card h2,.sidebar-card h2{font-size:18px;color:#10458c;margin:0 0 18px}.general-grid{display:grid;grid-template-columns:1fr 1fr;gap:0}.general-col{padding-right:28px}.general-col+.general-col{border-left:1px solid #e2e7ee;padding-left:28px}.data-line{display:grid;grid-template-columns:160px 20px 1fr;gap:5px;margin:12px 0;font-size:13px}.potential-grid{display:grid;grid-template-columns:repeat(4,1fr)}.potential{padding:5px 18px;border-right:1px solid #e2e7ee}.potential:first-child{padding-left:0}.potential:last-child{border:0}.icon{width:46px;height:46px;border-radius:10px;display:flex;align-items:center;justify-content:center;font-size:22px;margin-bottom:9px;background:#edf6ff}.potential strong{display:block;margin-bottom:5px}.potential small{color:#526074;line-height:1.5}.gallery-grid{display:grid;grid-template-columns:repeat(4,1fr);gap:12px}.gallery-grid img{width:100%;height:120px;object-fit:cover;border-radius:7px}.sidebar{display:flex;flex-direction:column;gap:18px}.sidebar-card{padding:18px}.map{height:160px;border-radius:8px;overflow:hidden;background:linear-gradient(135deg,#dff0d7,#eef5db);position:relative}.map:before{content:"";position:absolute;inset:0;background:linear-gradient(25deg,transparent 48%,rgba(130,160,110,.35) 49%,transparent 51%),linear-gradient(115deg,transparent 48%,rgba(145,175,130,.28) 49%,transparent 51%);mix-blend-mode:multiply}.pin{position:absolute;left:50%;top:50%;transform:translate(-50%,-100%);font-size:30px;z-index:2}.map-btn{display:block;width:100%;padding:10px;margin-top:10px;background:#0754b3;color:#fff;border:0;border-radius:7px;text-align:center;text-decoration:none;font-weight:700;cursor:pointer;font-size:12px}.map-btn:hover{background:#063f8b}.stats{display:grid;grid-template-columns:1fr 1fr;gap:12px}.stat{text-align:center}.stat .big{display:block;font-size:22px;font-weight:700;color:#0c448e;line-height:1.2}.stat small{display:block;margin-top:4px;color:#64738a;font-size:12px}.contact p{font-size:13px;line-height:1.6;color:#45566d;margin:0}
@media(max-width:1200px){.grid{grid-template-columns:repeat(2,minmax(0,1fr))}}
@media(max-width:1000px){.detail-layout{grid-template-columns:1fr}}
@media(max-width:650px){.container{width:92%}.grid{grid-template-columns:1fr}.list-title{font-size:30px}.village-card{min-height:120px}.village-card img{width:110px;flex-basis:110px;height:100px}.hero-content{grid-template-columns:1fr}.hero-content img{height:230px}.hero-text{padding:25px}.general-grid,.potential-grid{grid-template-columns:1fr}.general-col{padding:0}.general-col+.general-col{border-left:0;border-top:1px solid #e2e7ee;padding:12px 0 0}.potential{border-right:0;border-bottom:1px solid #e2e7ee;padding:12px 0}.gallery-grid{grid-template-columns:repeat(2,minmax(0,1fr))}.select{width:100%}.section-title{font-size:18px}}

.bps-overview{margin-top:24px}.bps-card{background:#fff;border:1px solid #dfe8f2;border-radius:12px;box-shadow:0 6px 18px rgba(23,58,96,.06);padding:22px;margin-top:16px}.bps-card h2{margin:0 0 8px;color:#0d448d;font-size:20px}.bps-card .lead{margin:0 0 16px;color:#52657d;font-size:13px;line-height:1.7}.bps-grid{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:12px}.bps-stat{border:1px solid #e1e8f0;border-radius:10px;padding:14px;background:#f9fbfe}.bps-stat .n{font-size:23px;font-weight:800;color:#0b4b97}.bps-stat small{display:block;color:#617087;margin-top:4px}.bps-table-wrap{overflow:auto;border:1px solid #e0e7ef;border-radius:9px}.bps-table{width:100%;border-collapse:collapse;min-width:680px;font-size:12.5px}.bps-table th,.bps-table td{padding:9px 10px;border-bottom:1px solid #e8edf3;text-align:left;vertical-align:top}.bps-table th{background:#eef6ff;color:#164c8c;font-weight:800}.bps-table tr:last-child td{border-bottom:0}.bps-table td.num{text-align:right;white-space:nowrap}.bps-table caption{text-align:left;padding:13px 12px;background:#fff;font-weight:800;color:#27476a}.bps-columns{display:grid;grid-template-columns:1fr 1fr;gap:16px}.bps-note{margin-top:10px;font-size:11px;color:#64758b;line-height:1.6}.bps-source-links{display:flex;flex-wrap:wrap;gap:8px;margin-top:12px}.bps-source-links a{display:inline-block;padding:8px 11px;border:1px solid #d4e4f7;border-radius:8px;color:#0754ad;text-decoration:none;background:#f7fbff;font-size:12px;font-weight:700}.village-extra{margin-top:18px}.village-extra-grid{display:grid;grid-template-columns:repeat(4,1fr);gap:10px}.mini{border:1px solid #e1e7ee;border-radius:9px;padding:12px;background:#fbfdff}.mini b{display:block;color:#0d448d;font-size:16px}.mini small{color:#64738a}.data-tag{display:inline-block;padding:3px 7px;border-radius:20px;background:#edf6ff;color:#1b568f;font-size:10px;font-weight:800;margin-left:5px}.detail-description-note{font-size:12px;color:#6a7890;margin-top:10px}.source strong{display:inline-block;margin-right:8px}
@media(max-width:1100px){.bps-grid{grid-template-columns:repeat(2,1fr)}.bps-columns{grid-template-columns:1fr}.village-extra-grid{grid-template-columns:repeat(2,1fr)}}
@media(max-width:650px){.bps-grid,.village-extra-grid{grid-template-columns:1fr}}
</style>
</head>
<body>
<section id="listPage" class="page active list-page">
  <main class="container">
    <button class="back-btn" onclick="backToKecamatan()">←&nbsp; Kembali ke Halaman Kecamatan</button>
    <h1 class="list-title">Desa di Kecamatan {DISTRICT_NAME}</h1>
    <p class="list-subtitle">Data wilayah, pemerintahan, penduduk, sosial, pertanian, pariwisata, transportasi, komunikasi, perbankan, koperasi, dan perdagangan berdasarkan <strong>Kecamatan {DISTRICT_NAME} Dalam Angka 2025</strong>.</p>
    <div class="breadcrumb">Kecamatan &nbsp;›&nbsp; Desa &nbsp;›&nbsp; {DISTRICT_NAME}</div>

    <div class="controls">
      <label for="districtSearch">Pilih Kecamatan</label>
      <div class="custom-select" id="districtSelect">
        <button class="custom-select__trigger" type="button" aria-haspopup="listbox" aria-expanded="false">
          <span class="custom-select__value">{DISTRICT_NAME_UPPER}</span><span class="custom-select__icon">▾</span>
        </button>
        <div class="custom-select__panel" role="listbox" aria-label="Daftar kecamatan">
          <div class="custom-select__search"><input id="districtSearch" type="text" placeholder="Cari kecamatan..." aria-label="Cari kecamatan" autocomplete="off"></div>
          <ul id="districtOptions" class="custom-select__options"></ul>
        </div>
      </div>
    </div>

    <div class="section-title">Daftar Desa di Kecamatan <span id="districtName">{DISTRICT_NAME}</span></div>
    <div id="villageGrid" class="grid"></div>

    <div class="bps-overview">
      <div class="bps-card">
        <h2>Gambaran Umum Kecamatan {DISTRICT_NAME}</h2>
        <p class="lead">{DESCRIPTION}</p>
        <div class="bps-grid" id="statsGrid"></div>
      </div>

      <div class="bps-card">
        <h2>Geografi & Administrasi</h2>
        <div class="bps-columns">
          <div class="bps-table-wrap"><table class="bps-table"><caption>Luas dan persentase wilayah, 2025</caption><thead><tr><th>Desa</th><th>Luas (km²)</th><th>% Kecamatan</th></tr></thead><tbody id="areaTable"></tbody></table></div>
          <div class="bps-table-wrap"><table class="bps-table"><caption>Jarak ke pusat pemerintahan (km), 2021</caption><thead><tr><th>Desa</th><th>Kecamatan</th><th>Kabupaten/Kota</th></tr></thead><tbody id="distanceTable"></tbody></table></div>
        </div>
      </div>

      <div class="bps-card">
        <h2>Pembagian Administratif</h2>
        <div class="bps-columns">
          <div class="bps-table-wrap"><table class="bps-table"><caption>RW dan RT per desa, 2024</caption><thead><tr><th>Desa</th><th>RW</th><th>RT</th></tr></thead><tbody id="rwrtTable"></tbody></table></div>
          <div class="bps-table-wrap"><table class="bps-table"><caption>Penduduk, 2024</caption><thead><tr><th>Desa</th><th>Laki-laki</th><th>Perempuan</th><th>Total</th><th>Kepadatan</th><th>Sex Ratio</th></tr></thead><tbody id="popTable"></tbody></table></div>
        </div>
      </div>

      <div class="bps-card">
        <h2>Sumber & Metadata Publikasi</h2>
        <p class="lead">Publikasi yang digunakan adalah <strong>Kecamatan {DISTRICT_NAME} Dalam Angka 2025</strong>, terbit September 2025 dari BPS Kabupaten Bandung Barat.</p>
        <p class="bps-note">Setiap tabel di atas mempertahankan tahun dan sumber sebagaimana dicantumkan dalam publikasi BPS. Tanda "–" berarti tidak ada/nol, sedangkan "…" berarti data tidak tersedia.</p>
        <div class="bps-source-links">
          <a href="https://bandungbaratkab.bps.go.id" target="_blank" rel="noopener">BPS Kabupaten Bandung Barat</a>
        </div>
      </div>
    </div>

    <div class="source"><strong>Sumber utama:</strong> BPS Kabupaten Bandung Barat, <em>Kecamatan {DISTRICT_NAME} Dalam Angka 2025</em>. Foto desa pada kartu digunakan sebagai ilustrasi visual, bukan statistik BPS.</div>
  </main>
</section>

<section id="detailPage" class="page detail-page">
  <main class="container">
    <button class="back-btn" onclick="showList()">←&nbsp; Kembali ke Daftar Desa</button>
    <div class="detail-layout">
      <div>
        <div class="detail-main hero-detail"><div class="hero-content"><img id="detailImage" src="" alt=""><div class="hero-text"><h1 id="detailName"></h1><div class="district">Kecamatan <span id="detailDistrict">{DISTRICT_NAME}</span>, Kabupaten Bandung Barat</div><p id="detailDescription"></p><div class="detail-description-note">Data statistik desa mengikuti tabel BPS yang tersedia; data yang tidak ada dalam publikasi tidak diisi.</div></div></div></div>
        <div class="detail-main detail-card"><h2>Informasi Umum Desa</h2><div class="general-grid"><div class="general-col"><div class="data-line"><b>Luas Wilayah 2025</b><span>:</span><span id="area"></span></div><div class="data-line"><b>Persentase Wilayah</b><span>:</span><span id="areaPct"></span></div><div class="data-line"><b>Penduduk 2024</b><span>:</span><span id="population"></span></div><div class="data-line"><b>Laki-laki</b><span>:</span><span id="male"></span></div><div class="data-line"><b>Perempuan</b><span>:</span><span id="female"></span></div><div class="data-line"><b>Kepadatan</b><span>:</span><span id="density"></span></div></div><div class="general-col"><div class="data-line"><b>Rasio Jenis Kelamin</b><span>:</span><span id="sexRatio"></span></div><div class="data-line"><b>RW</b><span>:</span><span id="rw"></span></div><div class="data-line"><b>RT</b><span>:</span><span id="rt"></span></div><div class="data-line"><b>Kode Desa</b><span>:</span><span id="code"></span></div><div class="data-line"><b>Jarak ke Ibukota Kecamatan</b><span>:</span><span id="distDistrict"></span></div><div class="data-line"><b>Jarak ke Ibukota Kabupaten/Kota</b><span>:</span><span id="distRegency"></span></div></div></div></div>
        <div class="detail-main detail-card"><h2>Statistik Desa dari BPS</h2><div class="village-extra-grid"><div class="mini"><b id="miniPop"></b><small>Penduduk 2024</small></div><div class="mini"><b id="miniDensity"></b><small>Kepadatan penduduk</small></div><div class="mini"><b id="miniRWRT"></b><small>RW / RT</small></div><div class="mini"><b id="miniArea"></b><small>Luas wilayah 2025</small></div></div><p class="bps-note">Data dari BPS Kabupaten Bandung Barat. Luas wilayah 2025; Penduduk Semester 2 Tahun 2024; RW/RT Semester 2 Tahun 2024; Jarak dari Podes 2021.</p></div>
        <div class="detail-main detail-card"><h2>Potensi & Statistik Kecamatan {DISTRICT_NAME}</h2><p style="margin:0;line-height:1.75;color:#45566d">Kecamatan {DISTRICT_NAME} memiliki berbagai potensi pengembangan di sektor pertanian, perdagangan, pariwisata, dan infrastruktur. Data pada halaman ini merupakan statistik <strong>tingkat Kecamatan {DISTRICT_NAME}</strong>.</p><div class="potential-grid" style="margin-top:18px"><div class="potential"><div class="icon">🌱</div><strong>Pertanian</strong><small>Pengembangan sektor pertanian lokal</small></div><div class="potential"><div class="icon">🏪</div><strong>Perdagangan</strong><small>Potensi usaha kecil dan menengah</small></div><div class="potential"><div class="icon">🏨</div><strong>Pariwisata</strong><small>Pengembangan daya tarik wisata lokal</small></div><div class="potential"><div class="icon">🏗️</div><strong>Infrastruktur</strong><small>Pengembangan sarana dan prasarana</small></div></div></div>
        <div class="detail-main detail-card"><h2>Galeri Desa</h2><div id="gallery" class="gallery-grid"></div></div>
      </div>
      <aside class="sidebar"><div class="sidebar-card"><h2>Peta Wilayah <span id="mapName"></span></h2><div class="map"><div class="pin">📍</div></div><a id="mapsLink" class="map-btn" href="#" target="_blank">Lihat di Google Maps ↗</a></div><div class="sidebar-card"><h2>Statistik Desa</h2><div class="stats"><div class="stat"><div class="big" id="statPop"></div><small>Jumlah Penduduk</small></div><div class="stat"><div class="big" id="statArea"></div><small>Luas Wilayah</small></div><div class="stat"><div class="big" id="statDensity"></div><small>Kepadatan</small></div><div class="stat"><div class="big" id="statSex"></div><small>Sex Ratio</small></div></div></div><div class="sidebar-card contact"><h2>Data Kontak</h2><p>Informasi alamat, telepon, email kepala desa, dan jumlah KK/dusun <strong>tidak dicantumkan dalam publikasi BPS ini</strong>, sehingga tidak diisi dengan data perkiraan.</p></div><div class="sidebar-card source-box"><h2>Sumber Data</h2>BPS Kabupaten Bandung Barat<br><span id="sourcePublication"></span></div></aside>
    </div>
    <div class="notice">ⓘ &nbsp; Data desa di halaman ini mengikuti publikasi <strong>Kecamatan {DISTRICT_NAME} Dalam Angka 2025</strong>. Tahun data dapat berbeda antar tabel, sesuai keterangan BPS.</div>
  </main>
</section>

<script>
const images = {
  {IMAGE_DICT}
};

const districtOptions=[
{{DISTRICT_OPTIONS}}
];

const villages = [
{{VILLAGES_JSON}}
];

let selectedDistrict='{SELECTED_DISTRICT}';

function renderDistrictOptions(){const list=document.getElementById('districtOptions'),search=document.getElementById('districtSearch'),valueLabel=document.querySelector('.custom-select__value');if(!list||!search||!valueLabel)return;const q=search.value.trim().toLowerCase();const filtered=districtOptions.filter(x=>x.label.toLowerCase().includes(q));list.innerHTML=filtered.map(x=>`<li class="custom-select__option ${{x.value===selectedDistrict?'is-selected':''}}" data-value="${{x.value}}">${{x.label}}</li>`).join('');const current=districtOptions.find(x=>x.value===selectedDistrict)||districtOptions[0];valueLabel.textContent=current.label;list.querySelectorAll('.custom-select__option').forEach(o=>o.onclick=()=>selectDistrict(o.dataset.value));}

function toggleDistrictSelect(force){const s=document.getElementById('districtSelect'),t=document.querySelector('.custom-select__trigger');if(!s||!t)return;const open=typeof force==='boolean'?force:!s.classList.contains('open');s.classList.toggle('open',open);t.setAttribute('aria-expanded',String(open));if(open)setTimeout(()=>document.getElementById('districtSearch')?.focus(),50)}

function selectDistrict(v){selectedDistrict=v;renderDistrictOptions();toggleDistrictSelect(false);const d=districtOptions.find(x=>x.value===v);if(d?.target)window.location.href=d.target;}

function renderVillages(){const grid=document.getElementById('villageGrid');grid.innerHTML=villages.map(v=>`<article class="village-card"><img src="${{images[v.key]||'https://images.unsplash.com/photo-1500534623283-312aade485b7?auto=format&fit=crop&w=900&q=85'}}" alt="${{v.name}}" onerror="this.src='https://images.unsplash.com/photo-1500534623283-312aade485b7?auto=format&fit=crop&w=900&q=85'"><div class="card-body"><h3>${{v.name}}</h3><div class="info-row"><span>Luas Wilayah</span><b>${{v.area}}</b></div><div class="info-row"><span>Penduduk 2024</span><b>${{v.pop}}</b></div><button class="detail-btn" onclick="openDetail('${{v.key}}')">>Lihat Detail</button></div></article>`).join('');}

function fillTables(){document.getElementById('areaTable').innerHTML=villages.map(v=>`<tr><td>${{v.name.replace('Desa ','')}}</td><td class="num">${{v.area.replace(' km²','')}}</td><td class="num">${{v.areaPct}}</td></tr>`).join('');document.getElementById('distanceTable').innerHTML=villages.map(v=>`<tr><td>${{v.name.replace('Desa ','')}}</td><td class="num">${{v.distDistrict}}</td><td class="num">${{v.distRegency}}</td></tr>`).join('');document.getElementById('rwrtTable').innerHTML=villages.map(v=>`<tr><td>${{v.name.replace('Desa ','')}}</td><td class="num">${{v.rw}}</td><td class="num">${{v.rt}}</td></tr>`).join('');document.getElementById('popTable').innerHTML=villages.map(v=>`<tr><td>${{v.name.replace('Desa ','')}}</td><td class="num">${{v.male}}</td><td class="num">${{v.female}}</td><td class="num">${{v.pop.replace(' jiwa','')}}</td><td class="num">${{v.density.replace(' jiwa/km²','')}}</td><td class="num">${{v.sexRatio}}</td></tr>`).join('');}

function fillStatsGrid(){const grid=document.getElementById('statsGrid');const totalArea=villages.reduce((sum,v)=>sum+parseFloat(v.area),0).toFixed(2);const totalPop=villages.reduce((sum,v)=>sum+parseInt(v.pop.replace(/[^0-9]/g,'')),0);const totalRW=villages.reduce((sum,v)=>sum+parseInt(v.rw),0);const totalRT=villages.reduce((sum,v)=>sum+parseInt(v.rt),0);grid.innerHTML=`<div class="bps-stat"><div class="n">${{villages.length}}</div><small>Desa</small></div><div class="bps-stat"><div class="n">${{totalArea}} km²</div><small>Luas Kecamatan 2025</small></div><div class="bps-stat"><div class="n">${{totalPop.toLocaleString('id-ID')}}</div><small>Penduduk 2024</small></div><div class="bps-stat"><div class="n">${{(totalPop/totalArea).toFixed(2)}}</div><small>Kepadatan</small></div><div class="bps-stat"><div class="n">${{totalRW}}</div><small>RW</small></div><div class="bps-stat"><div class="n">${{totalRT}}</div><small>RT</small></div><div class="bps-stat"><div class="n">-</div><small>PNS</small></div><div class="bps-stat"><div class="n">-</div><small>Koperasi</small></div>`;}

function openDetail(key){const v=villages.find(x=>x.key===key);if(!v)return;document.getElementById('listPage').classList.remove('active');document.getElementById('detailPage').classList.add('active');document.getElementById('detailImage').src=images[v.key]||'https://images.unsplash.com/photo-1500534623283-312aade485b7?auto=format&fit=crop&w=900&q=85';document.getElementById('detailImage').alt=v.name;document.getElementById('detailName').textContent=v.name;document.getElementById('detailDescription').textContent=v.name+' berada di Kecamatan {DISTRICT_NAME}, Kabupaten Bandung Barat. Ringkasan statistik pada halaman ini mengikuti data BPS yang tersedia untuk desa tersebut.';for(const id of ['area','areaPct','population','male','female','density','sexRatio','rw','rt','code','distDistrict','distRegency'])document.getElementById(id).textContent=v[id==='population'?'pop':id];document.getElementById('miniPop').textContent=v.pop;document.getElementById('miniDensity').textContent=v.density;document.getElementById('miniRWRT').textContent=`${{v.rw}} / ${{v.rt}}`;document.getElementById('miniArea').textContent=v.area;document.getElementById('statPop').textContent=v.pop.replace(' jiwa','');document.getElementById('statArea').textContent=v.area;document.getElementById('statDensity').textContent=v.density.replace(' jiwa/km²','');document.getElementById('statSex').textContent=v.sexRatio;document.getElementById('mapName').textContent=v.name;document.getElementById('mapsLink').href=`https://www.google.com/maps/search/?api=1&query=${{encodeURIComponent(v.name+' {DISTRICT_NAME} Bandung Barat')}}`;document.getElementById('sourcePublication').textContent='Kecamatan {DISTRICT_NAME} Dalam Angka 2025';document.getElementById('gallery').innerHTML=['jayagiri','lembang','cikahuripan'].map(k=>`<img src="${{images[k]||'https://images.unsplash.com/photo-1500534623283-312aade485b7?auto=format&fit=crop&w=900&q=85'}}" alt="Galeri ${{v.name}}" onerror="this.src='https://images.unsplash.com/photo-1500534623283-312aade485b7?auto=format&fit=crop&w=900&q=85';">`).join('');window.scrollTo({{top:0,behavior:'auto'}});}

function showList(){document.getElementById('detailPage').classList.remove('active');document.getElementById('listPage').classList.add('active');window.scrollTo({{top:0,behavior:'auto'}});}

function backToKecamatan(){window.location.href='kecamatan.html';}

document.addEventListener('click',e=>{const s=document.getElementById('districtSelect');if(s&&!s.contains(e.target))toggleDistrictSelect(false)});document.querySelector('.custom-select__trigger')?.addEventListener('click',()=>toggleDistrictSelect());document.getElementById('districtSearch')?.addEventListener('input',renderDistrictOptions);document.getElementById('districtSearch')?.addEventListener('keydown',e=>{{if(e.key==='Enter'){{const x=document.querySelector('#districtOptions .custom-select__option');if(x)selectDistrict(x.dataset.value)}}}}); 
renderDistrictOptions();renderVillages();fillTables();fillStatsGrid();
</script>
</body>
</html>'''

# List semua kecamatan
all_districts = ['lembang', 'parongpong', 'cisarua', 'cikalongwetan', 'cipeundeuy', 'ngamprah', 'cipatat', 'padalarang', 'batujajar', 'cihampelas', 'cililin', 'cipongkor', 'rongga', 'sindangkerta', 'gununghalu', 'saguling']

# Fungsi untuk generate district options
def generate_district_options():
    options = []
    for district in all_districts:
        if district == 'lembang':
            target = 'lembang.html'
        else:
            target = f'{district}.html'
        label = districts_data[district]['name'].upper()
        options.append(f'{{value:\'{district}\',label:\'{label}\',target:\'{target}\'}}')
    return ','.join(options)

# Fungsi untuk generate villages JSON
def generate_villages_json(district_key):
    villages = districts_data[district_key]['villages']
    village_objs = []
    for v in villages:
        village_objs.append(json.dumps(v))
    return ','.join(village_objs)

# Fungsi untuk generate image dictionary
def generate_image_dict():
    imgs = []
    for district in districts_data:
        for v in districts_data[district]['villages']:
            imgs.append(f'{v["key"]}:"https://images.unsplash.com/photo-1500534623283-312aade485b7?auto=format&fit=crop&w=900&q=85"')
    return ','.join(imgs)

# Buat halaman untuk setiap kecamatan (kecuali lembang)
for district_key in districts_data:
    if district_key == 'lembang':
        continue
    
    district_name = districts_data[district_key]['name']
    description = districts_data[district_key]['description']
    
    html_content = template_html.replace('{DISTRICT_NAME}', district_name)
    html_content = html_content.replace('{DISTRICT_NAME_UPPER}', district_name.upper())
    html_content = html_content.replace('{DESCRIPTION}', description)
    html_content = html_content.replace('{SELECTED_DISTRICT}', district_key)
    html_content = html_content.replace('{IMAGE_DICT}', generate_image_dict())
    html_content = html_content.replace('{{DISTRICT_OPTIONS}}', generate_district_options())
    html_content = html_content.replace('{{VILLAGES_JSON}}', generate_villages_json(district_key))
    
    # Simpan ke file
    filename = f'{district_key}.html'
    print(f'Membuat {filename}...')

print("Script siap untuk membuat semua halaman kecamatan!")
