# Digital Signal Processing Projects

Signal processing apps we built as a team during our biomedical engineering degree (Python/PyQt, plus a C++ FFT with pybind11).

## Try it online

These now run in the browser in [BioMed Lab](https://mohamed-halemo.github.io/biomed-lab/), no install needed:

| Folder | What it does | Try it |
|---|---|---|
| Signal Viewer app | ECG viewer, equalizer, sampling and aliasing | [ECG viewer →](https://mohamed-halemo.github.io/biomed-lab/#/ecg) |
| Fourier transform and fft | Recursive FFT vs DFT (C++ + pybind11) | [FFT explorer →](https://mohamed-halemo.github.io/biomed-lab/#/fft) |
| Images mixer | Mix the magnitude of one image with the phase of another | [Image mixer →](https://mohamed-halemo.github.io/biomed-lab/#/mixer) |
| Z-transform and plotting website | Place poles and zeros, see the frequency response | [Z-transform designer →](https://mohamed-halemo.github.io/biomed-lab/#/ztransform) |
| Shazam Like app | Spectrogram features and song matching | [Audio fingerprinting →](https://mohamed-halemo.github.io/biomed-lab/#/fingerprint) |

## Run the desktop versions

Each folder is its own app with its own `requirements.txt`.

| App | Run |
|---|---|
| Signal Viewer app | `pip install -r requirements.txt` then `python FinalV.py` |
| Images mixer | `pip install -r requirements.txt` then `python main.py` |
| Shazam Like app | `pip install -r requirements.txt` then `python project.py`. Put your own `.wav` songs in a `Songs/` folder first (none are included). |
| Z-transform and plotting website | `pip install -r requirements.txt` then `bokeh serve --show Main.py` |
| Fourier transform and fft | Build the C++ module with CMake (below) or open `Fourier/Fourier.sln` in Visual Studio. |

Build the FFT module (pybind11 is not included, so clone it first):

```bash
cd "Fourier transform and fft/pybind11-tutorial-master"
git clone --depth 1 -b v2.6.2 https://github.com/pybind/pybind11 externals/pybind11
cmake -B build && cmake --build build
```

## Team

[Mohamed Hafez](https://github.com/mohamed-halemo) · [Yumna Hamdy](https://github.com/Yumna-Hamdy) · [Mohamed Fathy](https://github.com/FathyJr10) · [Ahmed Osama](https://github.com/ahmedosama8)
