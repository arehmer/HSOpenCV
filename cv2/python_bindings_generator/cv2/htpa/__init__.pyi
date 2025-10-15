__all__: list[str] = []

import cv2
import cv2.typing
import typing as _typing


# Enumerations
HTPA60x40D_L1K9_0K8: int
HTPA60X40D_L1K9_0K8: int
HTPA120x84DR2_L3K95_0K8: int
HTPA120X84DR2_L3K95_0K8: int
HTPA160x120DR1_L3K95_0K8: int
HTPA160X120DR1_L3K95_0K8: int
HTPA8x8DR1_L0K8_0K8: int
HTPA8X8DR1_L0K8_0K8: int
HTPA32x32dR2_L1k9_0k8: int
HTPA32X32D_R2_L1K9_0K8: int
HTPA80x64dR2_L10k5_0k95_F7k7: int
HTPA80X64D_R2_L10K5_0K95_F7K7: int
HTPA32x32dR2_L1k7_0k8: int
HTPA32X32D_R2_L1K7_0K8: int
SENSOR_TYPE_NONE: int
SensorType = int
"""One of [HTPA60x40D_L1K9_0K8, HTPA60X40D_L1K9_0K8, HTPA120x84DR2_L3K95_0K8, HTPA120X84DR2_L3K95_0K8, HTPA160x120DR1_L3K95_0K8, HTPA160X120DR1_L3K95_0K8, HTPA8x8DR1_L0K8_0K8, HTPA8X8DR1_L0K8_0K8, HTPA32x32dR2_L1k9_0k8, HTPA32X32D_R2_L1K9_0K8, HTPA80x64dR2_L10k5_0k95_F7k7, HTPA80X64D_R2_L10K5_0K95_F7K7, HTPA32x32dR2_L1k7_0k8, HTPA32X32D_R2_L1K7_0K8, SENSOR_TYPE_NONE]"""



# Classes
class ClassifierEngine:
    ...

class ClassEngLinSVM(ClassifierEngine):
    ...

class df_row:
    idx: int
    xtl: int
    ytl: int
    xbr: int
    ybr: int
    w: int
    h: int
    image_id: int
    score: float
    track: int
    strikes: int
    label: int
    IoU_max: float
    IoU_idxmax: int
    detector_idx: int

class DataFrame:
    @property
    def rows(self) -> _typing.Sequence[df_row]: ...
    @property
    def columns(self) -> _typing.Sequence[str]: ...

    # Functions
    @_typing.overload
    def __init__(self) -> None: ...
    @_typing.overload
    def __init__(self, n_rows: int) -> None: ...

    @_typing.overload
    def add_row(self, idx: int, xtl: int, ytl: int, xbr: int, ybr: int, image_id: int = ..., score: float = ..., track: int = ..., strikes: int = ..., label: int = ..., IoU_max: float = ..., IoU_idxmax: int = ..., detector_idx: int = ...) -> None: ...
    @_typing.overload
    def add_row(self, row: df_row) -> None: ...

    @_typing.overload
    def get_content(self, df_content: cv2.typing.MatLike | None = ...) -> cv2.typing.MatLike: ...
    @_typing.overload
    def get_content(self, df_content: cv2.UMat | None = ...) -> cv2.UMat: ...


class Detector:
    ...

class SubDetector(Detector):
    # Functions
    def create(self, feat_engine_: FeatureEngine, class_engine_: ClassifierEngine) -> Detector: ...

    @_typing.overload
    def process(self, img: cv2.typing.MatLike, mask: cv2.typing.MatLike, bbox_prop: DataFrame) -> DataFrame: ...
    @_typing.overload
    def process(self, img: cv2.UMat, mask: cv2.UMat, bbox_prop: DataFrame) -> DataFrame: ...


class TwoScaleDetector(Detector):
    @property
    def mint_condition(self) -> bool: ...

    # Functions
    def create(self, sensor: SensorType, detector1: SubDetector, detector2: SubDetector, preproc_engine_: PreprocEngine, prop_generator_: ProposalGenerator, postproc_engine_: PostprocEngine) -> Detector: ...

    @_typing.overload
    def process(self, img: cv2.typing.MatLike, img_idx: int, pre_process: bool, post_process: bool, img_preproc: cv2.typing.MatLike | None = ...) -> tuple[DataFrame, cv2.typing.MatLike]: ...
    @_typing.overload
    def process(self, img: cv2.UMat, img_idx: int, pre_process: bool, post_process: bool, img_preproc: cv2.UMat | None = ...) -> tuple[DataFrame, cv2.UMat]: ...

    @_typing.overload
    def predict_bboxes(self, img: cv2.typing.MatLike, bboxes: DataFrame) -> DataFrame: ...
    @_typing.overload
    def predict_bboxes(self, img: cv2.UMat, bboxes: DataFrame) -> DataFrame: ...

    @_typing.overload
    def propose(self, img: cv2.typing.MatLike, img_idx: int, pre_process: bool, img_preproc: cv2.typing.MatLike | None = ..., mask: cv2.typing.MatLike | None = ...) -> tuple[DataFrame, cv2.typing.MatLike, cv2.typing.MatLike]: ...
    @_typing.overload
    def propose(self, img: cv2.UMat, img_idx: int, pre_process: bool, img_preproc: cv2.UMat | None = ..., mask: cv2.UMat | None = ...) -> tuple[DataFrame, cv2.UMat, cv2.UMat]: ...


class OneScaleDetector(TwoScaleDetector):
    # Functions
    def create(self, sensor: SensorType, subdetector: SubDetector, preproc_engine_: PreprocEngine, prop_generator_: ProposalGenerator, postproc_engine_: PostprocEngine) -> Detector: ...


class FeatureEngine:
    ...

class StatisticFeatEng(FeatureEngine):
    # Functions
    def create(self, sensor: SensorType, histN: int, histStart: int, histEnd: int) -> FeatureEngine: ...


class FeatEngHOG(FeatureEngine):
    # Functions
    def create(self, dw_size_: cv2.typing.Size, cell_size: int, block_size: int, block_stride: int, num_bins: int, signedGradient: bool, n_padding: int) -> FeatureEngine: ...


class FeatEngHOGdK(FeatEngHOG):
    # Functions
    def create(self, dw_size_: cv2.typing.Size, cell_size: int, block_size: int, block_stride: int, num_bins: int, signedGradient: bool, n_padding: int, histN: int, histStart: int, histEnd: int) -> FeatureEngine: ...

    @_typing.overload
    def process(self, img: cv2.typing.MatLike, mask: cv2.typing.MatLike, bbox_prop: DataFrame, X_feat: cv2.typing.MatLike | None = ...) -> cv2.typing.MatLike: ...
    @_typing.overload
    def process(self, img: cv2.UMat, mask: cv2.UMat, bbox_prop: DataFrame, X_feat: cv2.UMat | None = ...) -> cv2.UMat: ...


class Filter:
    ...

class AWA_Filter(Filter):
    @property
    def width_(self) -> int: ...
    @property
    def height_(self) -> int: ...
    @property
    def K_(self) -> int: ...
    @property
    def S_(self) -> int: ...
    @property
    def a_(self) -> float: ...
    @property
    def eps_(self) -> int: ...

    # Functions
    def create(self, sensor: SensorType, K: int, S: int, a: float, eps: int) -> Filter: ...

    @_typing.overload
    def filter(self, img: cv2.typing.MatLike, img_idx: int, img_filt: cv2.typing.MatLike | None = ...) -> tuple[int, cv2.typing.MatLike]: ...
    @_typing.overload
    def filter(self, img: cv2.UMat, img_idx: int, img_filt: cv2.UMat | None = ...) -> tuple[int, cv2.UMat]: ...

    def reset(self) -> None: ...

    def set_a(self, a: float) -> None: ...

    def set_eps(self, eps: int) -> None: ...

    def get_width(self) -> int: ...

    def get_height(self) -> int: ...

    def get_filtered_img(self) -> cv2.typing.MatLike: ...


class HTPAFileReader:
    # Functions
    def read_file(self, file_path: str) -> None: ...


class PostprocEngine:
    ...

class PostprocEng_NMS(PostprocEngine):
    # Functions
    @_typing.overload
    def __init__(self) -> None: ...
    @_typing.overload
    def __init__(self, IoU_thresh: float, filter_nested: bool) -> None: ...

    def create(self, IoU_thresh: float, filter_nested: bool) -> PostprocEngine: ...

    def process(self, bboxes: DataFrame, label: int) -> DataFrame: ...


class PreprocEngine:
    ...

class PreprocEngAWA(PreprocEngine):
    # Functions
    def create(self, sensor: SensorType, K: int, S: int, a: float, eps: int) -> PreprocEngine: ...

    @_typing.overload
    def process(self, img: cv2.typing.MatLike, img_idx: int, img_proc: cv2.typing.MatLike | None = ...) -> tuple[int, cv2.typing.MatLike]: ...
    @_typing.overload
    def process(self, img: cv2.UMat, img_idx: int, img_proc: cv2.UMat | None = ...) -> tuple[int, cv2.UMat]: ...


class ProposalGenerator:
    ...

class PropGenWatershed_v1(ProposalGenerator):
    # Functions
    @_typing.overload
    def create(self, sensor: SensorType, array_mask: cv2.typing.MatLike, otsu_q: float, otsu_res: int, bbsize_min: cv2.typing.Size, bbsize_max: cv2.typing.Size, bbox_reg_coef: _typing.Sequence[float] = ..., bbox_reg_inter: _typing.Sequence[float] = ...) -> ProposalGenerator: ...
    @_typing.overload
    def create(self, sensor: SensorType, array_mask: cv2.UMat, otsu_q: float, otsu_res: int, bbsize_min: cv2.typing.Size, bbsize_max: cv2.typing.Size, bbox_reg_coef: _typing.Sequence[float] = ..., bbox_reg_inter: _typing.Sequence[float] = ...) -> ProposalGenerator: ...


class htpa_file:
    pixel: _typing.Sequence[_typing.Sequence[int]]
    eoffset: _typing.Sequence[_typing.Sequence[int]]
    vdd: _typing.Sequence[_typing.Sequence[int]]
    tamb: _typing.Sequence[_typing.Sequence[int]]
    ptat: _typing.Sequence[_typing.Sequence[int]]
    atc: _typing.Sequence[_typing.Sequence[int]]
    header: str

class TPArray:
    @property
    def w(self) -> int: ...
    @property
    def h(self) -> int: ...
    @property
    def resolution(self) -> cv2.typing.Size: ...

    # Functions
    @_typing.overload
    def __init__(self) -> None: ...
    @_typing.overload
    def __init__(self, sensorType: SensorType) -> None: ...

    def get_radiometric_mask(self) -> cv2.typing.MatLike: ...


class Thresholder:
    ...

class HSOtsuThresh(Thresholder):
    # Functions
    def create(self, percentile: float, th_res_: int, mask: cv2.typing.MatLike, thresh_type: cv2.ThresholdTypes = ..., maxval: float = ...) -> Thresholder: ...

    @_typing.overload
    def threshold(self, img: cv2.typing.MatLike, img_thresh: cv2.typing.MatLike | None = ...) -> cv2.typing.MatLike: ...
    @_typing.overload
    def threshold(self, img: cv2.UMat, img_thresh: cv2.UMat | None = ...) -> cv2.UMat: ...


class HSMultiOtsu(HSOtsuThresh):
    # Functions
    def create(self, percentile: float, th_res_: int, mask: cv2.typing.MatLike, thresh_type: cv2.ThresholdTypes = ..., maxval: float = ...) -> Thresholder: ...

    @_typing.overload
    def threshold(self, img: cv2.typing.MatLike, img_thresh: cv2.typing.MatLike | None = ...) -> cv2.typing.MatLike: ...
    @_typing.overload
    def threshold(self, img: cv2.UMat, img_thresh: cv2.UMat | None = ...) -> cv2.UMat: ...


class Tracker:
    ...

class block:
    xy: cv2.typing.Point
    B: cv2.typing.MatLike
    B_weights: cv2.typing.MatLike
    avg_dist: int

class target_model:
    tl: block
    bl: block
    br: block
    tr: block

class BlockTracker(Tracker):
    # Functions
    @_typing.overload
    def __init__(self) -> None: ...
    @_typing.overload
    def __init__(self, allowed_shifts: _typing.Sequence[int]) -> None: ...
    @_typing.overload
    def __init__(self, tparray: TPArray, allowed_shifts: _typing.Sequence[int]) -> None: ...

    @_typing.overload
    def track_roi(self, frame: cv2.typing.MatLike, bbox: df_row) -> None: ...
    @_typing.overload
    def track_roi(self, frame: cv2.UMat, bbox: df_row) -> None: ...


class Tracktor:
    ...

class DummyTracktor(Tracktor):
    # Functions
    @_typing.overload
    def __init__(self) -> None: ...
    @_typing.overload
    def __init__(self, detector: TwoScaleDetector) -> None: ...

    @_typing.overload
    def track(self, frame: cv2.typing.MatLike, img_idx: int, proc_frame: cv2.typing.MatLike | None = ...) -> tuple[DataFrame, cv2.typing.MatLike]: ...
    @_typing.overload
    def track(self, frame: cv2.UMat, img_idx: int, proc_frame: cv2.UMat | None = ...) -> tuple[DataFrame, cv2.UMat]: ...


class BlockTracktor(Tracktor):
    # Functions
    @_typing.overload
    def __init__(self) -> None: ...
    @_typing.overload
    def __init__(self, detector: TwoScaleDetector, s_active: float, s_init: float, IoU_active: float, IoU_init: float, strikes_lim: int, score_lim_del: float, alpha: int, pix_shift: _typing.Sequence[int]) -> None: ...

    @_typing.overload
    def track(self, frame: cv2.typing.MatLike, img_idx: int, proc_frame: cv2.typing.MatLike | None = ...) -> tuple[DataFrame, cv2.typing.MatLike]: ...
    @_typing.overload
    def track(self, frame: cv2.UMat, img_idx: int, proc_frame: cv2.UMat | None = ...) -> tuple[DataFrame, cv2.UMat]: ...



