# import streamlit as st
# import pandas as pd
# import joblib

# # ===============================
# # LOAD MODEL
# # ===============================
# MODEL_PATH = "model_decision_tree_literasi_sd.pkl"
# model_dt = joblib.load(MODEL_PATH)

# # ===============================
# # DATA SOAL PRE-TEST
# # ===============================
# soal_pretest = [
#     {
#         "pertanyaan": "1. Hasil dari 8 + 5 adalah ...",
#         "opsi": ["10", "12", "13", "14"],
#         "jawaban": "13"
#     },
#     {
#         "pertanyaan": "2. Hasil dari 10 - 4 adalah ...",
#         "opsi": ["5", "6", "7", "8"],
#         "jawaban": "6"
#     },
#     {
#         "pertanyaan": "3. Hasil dari 3 × 4 adalah ...",
#         "opsi": ["7", "10", "12", "14"],
#         "jawaban": "12"
#     }
# ]

# # ===============================
# # MATERI ADAPTIF
# # ===============================
# materi = {
#     "normal": """
#     Penjumlahan dan pengurangan adalah operasi dasar matematika.
#     Perkalian merupakan penjumlahan berulang.
#     """,
#     "sederhana": """
#     Penjumlahan artinya menambah angka.
#     Pengurangan artinya mengurangi angka.
#     Perkalian artinya menjumlahkan angka yang sama berulang kali.
#     """
# }

# # ===============================
# # FUNGSI HITUNG PRETEST
# # ===============================
# def hitung_pretest(soal, jawaban_siswa):
#     benar = 0
#     for i in range(len(soal)):
#         if jawaban_siswa[i] == soal[i]["jawaban"]:
#             benar += 1

#     total = len(soal)
#     nilai = (benar / total) * 100
#     salah = total - benar
#     return nilai, salah

# # ===============================
# # STREAMLIT UI
# # ===============================
# st.set_page_config(page_title="Pembelajaran Adaptif AI", layout="centered")

# st.title("📘 Sistem Pembelajaran Adaptif Berbasis AI")
# st.subheader("Literasi Matematis SD")

# st.markdown("---")

# st.header("📝 Pre-Test")

# jawaban_siswa = []

# for i, soal in enumerate(soal_pretest):
#     jawaban = st.radio(
#         soal["pertanyaan"],
#         soal["opsi"],
#         key=f"soal_{i}"
#     )
#     jawaban_siswa.append(jawaban)

# waktu = st.slider("⏱️ Waktu pengerjaan (menit)", 5, 20, 10)

# # ===============================
# # PROSES PRETEST
# # ===============================
# if st.button("🔍 Proses Pre-Test"):
#     nilai, salah = hitung_pretest(soal_pretest, jawaban_siswa)

#     data_input = pd.DataFrame({
#         "nilai_pretest": [nilai],
#         "jumlah_salah": [salah],
#         "waktu": [waktu]
#     })

#     level = model_dt.predict(data_input)[0]

#     st.markdown("---")
#     st.header("📊 Hasil Evaluasi")

#     st.write(f"**Nilai Pre-test:** {nilai:.2f}")
#     st.write(f"**Jumlah Salah:** {salah}")
#     st.write(f"**Level Kemampuan:** `{level}`")

#     st.markdown("---")
#     st.header("📚 Materi Pembelajaran")

#     if level == "Rendah":
#         st.info(materi["sederhana"])
#     else:
#         st.success(materi["normal"])

#     st.markdown("---")
#     st.caption("Sistem menentukan tingkat kemampuan siswa menggunakan Decision Tree Learning")

# update2
# import streamlit as st
# import pandas as pd
# import joblib

# # =====================
# # LOAD MODEL
# # =====================
# model = joblib.load("model_decision_tree_literasi_sd.pkl")

# # =====================
# # SESSION STATE
# # =====================
# if "page" not in st.session_state:
#     st.session_state.page = "pretest"

# if "level" not in st.session_state:
#     st.session_state.level = None

# # =====================
# # SOAL PRETEST
# # =====================
# pretest_soal = [
#     ("8 + 5 =", ["10", "12", "13"], "13"),
#     ("10 - 4 =", ["5", "6", "7"], "6"),
#     ("3 × 4 =", ["10", "12", "14"], "12"),
# ]

# # =====================
# # SOAL POSTTEST
# # =====================
# posttest_soal = [
#     ("6 + 7 =", ["12", "13", "14"], "13"),
#     ("9 - 3 =", ["5", "6", "7"], "6"),
# ]

# # =====================
# # MATERI
# # =====================
# materi = {
#     "easy": {
#         "penjumlahan": "Penjumlahan berarti menambah angka. Contoh: 2 + 3 = 5",
#         "pengurangan": "Pengurangan berarti mengurangi angka. Contoh: 5 - 2 = 3",
#     },
#     "normal": {
#         "penjumlahan": "Penjumlahan adalah operasi matematika untuk menjumlahkan bilangan.",
#         "pengurangan": "Pengurangan adalah operasi matematika untuk mencari selisih.",
#         "perkalian": "Perkalian adalah penjumlahan berulang.",
#     }
# }

# # =====================
# # HITUNG NILAI
# # =====================
# def hitung_nilai(soal, jawaban):
#     benar = 0
#     for i in range(len(soal)):
#         if jawaban[i] == soal[i][2]:
#             benar += 1
#     nilai = (benar / len(soal)) * 100
#     return nilai, len(soal) - benar

# # =====================
# # HALAMAN PRETEST
# # =====================
# if st.session_state.page == "pretest":
#     st.title("📝 Pre-test")

#     jawaban = []
#     for i, soal in enumerate(pretest_soal):
#         j = st.radio(soal[0], soal[1], key=f"pre_{i}")
#         jawaban.append(j)

#     waktu = st.slider("Waktu pengerjaan (menit)", 5, 20, 10)

#     if st.button("Proses Pre-test"):
#         nilai, salah = hitung_nilai(pretest_soal, jawaban)

#         data = pd.DataFrame({
#             "nilai_pretest": [nilai],
#             "jumlah_salah": [salah],
#             "waktu": [waktu]
#         })

#         st.session_state.level = model.predict(data)[0]
#         st.session_state.page = "materi"
#         st.rerun()

# # =====================
# # HALAMAN MATERI
# # =====================
# elif st.session_state.page == "materi":
#     st.title("📘 Materi Pembelajaran")

#     level = st.session_state.level
#     st.write(f"**Level kemampuan:** {level}")

#     if level == "Rendah":
#         st.info(materi["easy"]["penjumlahan"])
#         st.info(materi["easy"]["pengurangan"])
#     else:
#         st.success(materi["normal"]["penjumlahan"])
#         st.success(materi["normal"]["pengurangan"])

#     if st.button("Lanjut ke Post-test"):
#         st.session_state.page = "posttest"
#         st.rerun()

# # =====================
# # HALAMAN POSTTEST
# # =====================
# elif st.session_state.page == "posttest":
#     st.title("🧪 Post-test")

#     jawaban = []
#     for i, soal in enumerate(posttest_soal):
#         j = st.radio(soal[0], soal[1], key=f"post_{i}")
#         jawaban.append(j)

#     if st.button("Proses Post-test"):
#         nilai, _ = hitung_nilai(posttest_soal, jawaban)

#         if nilai < 60:
#             st.error("Hasil rendah → ulang materi dengan bahasa mudah")
#             st.info(materi["easy"]["penjumlahan"])
#             st.info(materi["easy"]["pengurangan"])
#         else:
#             st.success("Hasil baik → lanjut ke materi perkalian")
#             st.success(materi["normal"]["perkalian"])

# update3
import streamlit as st
import joblib
import pandas as pd

# ================= LOAD MODEL =================
model = joblib.load("model_decision_tree_literasi_sd.pkl")

# ================= SESSION STATE =================
if "step" not in st.session_state:
    st.session_state.step = "pretest"

if "nilai_pretest" not in st.session_state:
    st.session_state.nilai_pretest = 0

if "level" not in st.session_state:
    st.session_state.level = None

if "jalur" not in st.session_state:
    st.session_state.jalur = None

if "nilai_posttest" not in st.session_state:
    st.session_state.nilai_posttest = 0

# ================= BEST FIRST SEARCH =================
def best_first_search(nilai):
    if nilai < 60:
        return "easy"
    else:
        return "normal"
    # else:
    #     return "advance"

# ================= MATERI =================
materi = {
    "easy": {
        "penjumlahan": "Penjumlahan adalah proses menggabungkan dua bilangan. Contoh: 1 + 1 = 2,",
        "pengurangan": "Pengurangan adalah proses mengurangi bilangan. Contoh: 1 - 1 = 0.",
    },
    "normal": {
        "penjumlahan": "Penjumlahan menggabungkan nilai bilangan secara matematis.",
        "pengurangan": "Pengurangan menentukan selisih dua bilangan.",
        "perkalian": "Perkalian adalah penjumlahan berulang. Contoh: 3 × 4 = 12."
    }
}

# ================= UI =================
st.title("📘 Sistem Pembelajaran Adaptif Matematika SD")

# =====================================================
# PRETEST
# =====================================================
if st.session_state.step == "pretest":
    st.header("📝 Pretest")

    q1 = st.radio("1. 3 + 2 = ?", [4, 5, 6])
    q2 = st.radio("2. 5 - 1 = ?", [3, 4, 5])
    q3 = st.radio("3. 2 + 4 = ?", [5, 6, 7])

    if st.button("Submit Pretest"):
        score = 0
        if q1 == 5: score += 33
        if q2 == 4: score += 33
        if q3 == 6: score += 34

        st.session_state.nilai_pretest = score

        # Data ke Decision Tree
        data = pd.DataFrame([[score, 3 - (score//33), 120]],
                             columns=["nilai_pretest", "jumlah_salah", "waktu"])

        level = model.predict(data)[0]
        jalur = best_first_search(score)

        st.session_state.level = level
        st.session_state.jalur = jalur
        st.session_state.step = "materi"

        st.rerun()

# =====================================================
# MATERI
# =====================================================
elif st.session_state.step == "materi":
    st.header("📖 Materi Pembelajaran")

    st.info(f"Tingkat kemampuan siswa: **{st.session_state.level}**")
    st.info(f"Jalur pembelajaran (BFS): **{st.session_state.jalur}**")

    if st.session_state.jalur == "easy":
        st.write("### Materi Bahasa Mudah")
        st.write(materi["easy"]["penjumlahan"])
        st.write(materi["easy"]["pengurangan"])

    else:
        st.write("### Materi Normal")
        st.write(materi["normal"]["penjumlahan"])
        st.write(materi["normal"]["pengurangan"])

    if st.button("Lanjut ke Posttest"):
        st.session_state.step = "posttest"
        st.rerun()

# =====================================================
# POSTTEST
# =====================================================
elif st.session_state.step == "posttest":
    st.header("🧪 Posttest")

    p1 = st.radio("1. 4 + 3 = ?", [6, 7, 8])
    p2 = st.radio("2. 6 - 2 = ?", [3, 4, 5])
    p3 = st.radio("3. 2 × 3 = ?", [5, 6, 7])

    if st.button("Submit Posttest"):
        score = 0
        if p1 == 7: score += 33
        if p2 == 4: score += 33
        if p3 == 6: score += 34

        st.session_state.nilai_posttest = score

        if score < 60:
            st.error("❌ Hasil rendah → Remedial otomatis")
            st.subheader("📖 Materi Remedial (Bahasa Mudah)")
            st.write(materi["easy"]["penjumlahan"])
            st.write(materi["easy"]["pengurangan"])

        else:
            st.success("✅ Lulus → Lanjut Materi Perkalian")
            st.subheader("📘 Materi Perkalian")
            st.write(materi["normal"]["perkalian"])
