---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: IGAD Climate Prediction and Applications Center (ICPAC)
  url: https://data.humdata.org/dataset/igad-region-dekadal-combined-drought-indicator-cdi-2025
creator:
  affiliation: null
  email: null
  name: IGAD Climate Prediction and Applications Center (ICPAC)
  url: https://data.humdata.org/dataset/igad-region-dekadal-combined-drought-indicator-cdi-2025
dataset_id: rdls_hzd-icpac_regiondekadalcombineddrou_2025
description: 'Dekadal (10 days) Combined Drought Indicator (CDI) as implemented in
  the East Africa Drought Watch, and which is used for detecting and monitoring areas
  that either are affected or have the potential to be affected by meteorological,
  agricultural and/or hydrological drought.. [Source: This metadata record was automatically
  extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/igad-region-dekadal-combined-drought-indicator-cdi-2025]'
details: In applying the classification scheme, a temporal lag between the three components
  of the CDI is implemented. Thus, SPI of a given month is contrasted with soil moisture
  anomalies of the 2nd and 3rd dekads of that month, and with the 1st dekad of the
  folowing month, and with FAPAR anomalies of the 3rd dekad of that month and the
  1st and 2nd dekads of the folowing month. Each month is assumed to have three dekads
  (days 1-10; days 11-20; day 21 to the end of the month).
exposure: []
hazard:
  event_sets_by_hazard_type:
    drought:
    - analysis_type: empirical
      calculation_method: simulated
      event_count: 0
      events: []
      frequency_distribution: null
      hazards:
      - classification: null
        id: hazard_1
        intensity_measure: CDI:-
        process: meteorological_drought
        trigger: null
        type: drought
      id: event_set_1
      occurrence_range: null
      seasonality: null
  event_sets_count: 1
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: The CDI is a composite drought monitoring index implemented by ICPAC's
    East Africa Drought Watch system, combining multiple drought indicators (meteorological,
    agricultural, hydrological) into dekadal (10-day) raster grids. The dataset provides
    continuous temporal monitoring of drought conditions across the IGAD region to
    detect and track areas affected by or at risk of drought.
  sources:
  - id: source_1
    license: null
    name: IGAD Climate Prediction and Applications Center (ICPAC)
    risk_data_type:
    - hazard
    type: model
    url: null
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/igad-region-dekadal-combined-drought-indicator-cdi-2025
  rel: source
loss:
  losses: []
project: null
publisher:
  affiliation: null
  email: null
  name: Humanitarian Data Exchange (HDX)
  url: https://data.humdata.org/
purpose: null
referenced_by:
- author_names: null
  date_published: null
  doi: null
  id: reference_1
  name: Methodology documentation
  url: https://droughtwatch.icpac.net/documents/3/EADW-CDI-Factsheet.pdf
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: IGAD Region - Dekadal Combined Drought Indicator (CDI) 2025 (Dekadal
    (10 days) Combined Drought Indicator (CDI) for 2025-01-01)
  download_url: https://data.humdata.org/dataset/21e997e2-81a9-4425-be59-3436641c55d1/resource/8dff8e15-f3da-4531-b7de-39fc54a3e275/download/eadw-cdi-data-2025-01-01.tif
  format: null
  id: resource_8dff8e15
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: eadw-cdi-data-2025-01-01.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: IGAD Region - Dekadal Combined Drought Indicator (CDI) 2025 (Dekadal
    (10 days) Combined Drought Indicator (CDI) for 2025-01-11)
  download_url: https://data.humdata.org/dataset/21e997e2-81a9-4425-be59-3436641c55d1/resource/0bee8c84-e335-421e-93b0-b7d350ba7feb/download/eadw-cdi-data-2025-01-11.tif
  format: null
  id: resource_0bee8c84
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: eadw-cdi-data-2025-01-11.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: IGAD Region - Dekadal Combined Drought Indicator (CDI) 2025 (Dekadal
    (10 days) Combined Drought Indicator (CDI) for 2025-01-21)
  download_url: https://data.humdata.org/dataset/21e997e2-81a9-4425-be59-3436641c55d1/resource/f595e0da-bc8d-4b57-96d4-d98115e1032c/download/eadw-cdi-data-2025-01-21.tif
  format: null
  id: resource_f595e0da
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: eadw-cdi-data-2025-01-21.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: IGAD Region - Dekadal Combined Drought Indicator (CDI) 2025 (Dekadal
    (10 days) Combined Drought Indicator (CDI) for 2025-02-01)
  download_url: https://data.humdata.org/dataset/21e997e2-81a9-4425-be59-3436641c55d1/resource/41ae8b8d-dd73-4e2e-b205-0cbc7cfbbddc/download/eadw-cdi-data-2025-02-01.tif
  format: null
  id: resource_41ae8b8d
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: eadw-cdi-data-2025-02-01.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: IGAD Region - Dekadal Combined Drought Indicator (CDI) 2025 (Dekadal
    (10 days) Combined Drought Indicator (CDI) for 2025-02-11)
  download_url: https://data.humdata.org/dataset/21e997e2-81a9-4425-be59-3436641c55d1/resource/7a62b113-93e6-4d57-8860-1fb3f76b59d7/download/eadw-cdi-data-2025-02-11.tif
  format: null
  id: resource_7a62b113
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: eadw-cdi-data-2025-02-11.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: IGAD Region - Dekadal Combined Drought Indicator (CDI) 2025 (Dekadal
    (10 days) Combined Drought Indicator (CDI) for 2025-02-21)
  download_url: https://data.humdata.org/dataset/21e997e2-81a9-4425-be59-3436641c55d1/resource/e459f2ef-8d0a-4345-a041-1eea2ff3f0b3/download/eadw-cdi-data-2025-02-21.tif
  format: null
  id: resource_e459f2ef
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: eadw-cdi-data-2025-02-21.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: IGAD Region - Dekadal Combined Drought Indicator (CDI) 2025 (Dekadal
    (10 days) Combined Drought Indicator (CDI) for 2025-03-01)
  download_url: https://data.humdata.org/dataset/21e997e2-81a9-4425-be59-3436641c55d1/resource/40e8abc3-fb26-4d47-80a2-f9f7cd48851d/download/eadw-cdi-data-2025-03-01.tif
  format: null
  id: resource_40e8abc3
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: eadw-cdi-data-2025-03-01.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: IGAD Region - Dekadal Combined Drought Indicator (CDI) 2025 (Dekadal
    (10 days) Combined Drought Indicator (CDI) for 2025-03-11)
  download_url: https://data.humdata.org/dataset/21e997e2-81a9-4425-be59-3436641c55d1/resource/a343587b-7aec-4d85-a029-672c93bf2e89/download/eadw-cdi-data-2025-03-11.tif
  format: null
  id: resource_a343587b
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: eadw-cdi-data-2025-03-11.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: IGAD Region - Dekadal Combined Drought Indicator (CDI) 2025 (Dekadal
    (10 days) Combined Drought Indicator (CDI) for 2025-03-21)
  download_url: https://data.humdata.org/dataset/21e997e2-81a9-4425-be59-3436641c55d1/resource/438d4d22-6617-4adb-aaf6-89c678117bfa/download/eadw-cdi-data-2025-03-21.tif
  format: null
  id: resource_438d4d22
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: eadw-cdi-data-2025-03-21.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: IGAD Region - Dekadal Combined Drought Indicator (CDI) 2025 (Dekadal
    (10 days) Combined Drought Indicator (CDI) for 2025-04-01)
  download_url: https://data.humdata.org/dataset/21e997e2-81a9-4425-be59-3436641c55d1/resource/d4abc56d-38c5-4e9e-a7d4-2d073fc7514e/download/eadw-cdi-data-2025-04-01.tif
  format: null
  id: resource_d4abc56d
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: eadw-cdi-data-2025-04-01.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: IGAD Region - Dekadal Combined Drought Indicator (CDI) 2025 (Dekadal
    (10 days) Combined Drought Indicator (CDI) for 2025-04-11)
  download_url: https://data.humdata.org/dataset/21e997e2-81a9-4425-be59-3436641c55d1/resource/137ab893-c96c-49eb-8e3c-f924f67d609a/download/eadw-cdi-data-2025-04-11.tif
  format: null
  id: resource_137ab893
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: eadw-cdi-data-2025-04-11.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: IGAD Region - Dekadal Combined Drought Indicator (CDI) 2025 (Dekadal
    (10 days) Combined Drought Indicator (CDI) for 2025-04-21)
  download_url: https://data.humdata.org/dataset/21e997e2-81a9-4425-be59-3436641c55d1/resource/2e66e441-dfb4-4a2b-88e7-1c16b662a6ad/download/eadw-cdi-data-2025-04-21.tif
  format: null
  id: resource_2e66e441
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: eadw-cdi-data-2025-04-21.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: IGAD Region - Dekadal Combined Drought Indicator (CDI) 2025 (Dekadal
    (10 days) Combined Drought Indicator (CDI) for 2025-05-01)
  download_url: https://data.humdata.org/dataset/21e997e2-81a9-4425-be59-3436641c55d1/resource/25ce9bf5-d096-4afc-bc69-67836327bef6/download/eadw-cdi-data-2025-05-01.tif
  format: null
  id: resource_25ce9bf5
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: eadw-cdi-data-2025-05-01.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: IGAD Region - Dekadal Combined Drought Indicator (CDI) 2025 (Dekadal
    (10 days) Combined Drought Indicator (CDI) for 2025-05-11)
  download_url: https://data.humdata.org/dataset/21e997e2-81a9-4425-be59-3436641c55d1/resource/75bac0e0-dfcd-4d8b-b05c-99d3d29c6cea/download/eadw-cdi-data-2025-05-11.tif
  format: null
  id: resource_75bac0e0
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: eadw-cdi-data-2025-05-11.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: IGAD Region - Dekadal Combined Drought Indicator (CDI) 2025 (Dekadal
    (10 days) Combined Drought Indicator (CDI) for 2025-05-21)
  download_url: https://data.humdata.org/dataset/21e997e2-81a9-4425-be59-3436641c55d1/resource/a05822dc-bbea-4666-b3d5-4e082c3bbb3f/download/eadw-cdi-data-2025-05-21.tif
  format: null
  id: resource_a05822dc
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: eadw-cdi-data-2025-05-21.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: IGAD Region - Dekadal Combined Drought Indicator (CDI) 2025 (Dekadal
    (10 days) Combined Drought Indicator (CDI) for 2025-06-01)
  download_url: https://data.humdata.org/dataset/21e997e2-81a9-4425-be59-3436641c55d1/resource/f6b78252-ae4b-4a7d-881e-d6a59a54635c/download/eadw-cdi-data-2025-06-01.tif
  format: null
  id: resource_f6b78252
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: eadw-cdi-data-2025-06-01.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: IGAD Region - Dekadal Combined Drought Indicator (CDI) 2025 (Dekadal
    (10 days) Combined Drought Indicator (CDI) for 2025-06-11)
  download_url: https://data.humdata.org/dataset/21e997e2-81a9-4425-be59-3436641c55d1/resource/5c3728c6-7605-4828-8324-b95aa8c03150/download/eadw-cdi-data-2025-06-11.tif
  format: null
  id: resource_5c3728c6
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: eadw-cdi-data-2025-06-11.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: IGAD Region - Dekadal Combined Drought Indicator (CDI) 2025 (Dekadal
    (10 days) Combined Drought Indicator (CDI) for 2025-06-21)
  download_url: https://data.humdata.org/dataset/21e997e2-81a9-4425-be59-3436641c55d1/resource/c796735c-468a-4817-a3a2-1b93f203cc7b/download/eadw-cdi-data-2025-06-21.tif
  format: null
  id: resource_c796735c
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: eadw-cdi-data-2025-06-21.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: IGAD Region - Dekadal Combined Drought Indicator (CDI) 2025 (Dekadal
    (10 days) Combined Drought Indicator (CDI) for 2025-07-01)
  download_url: https://data.humdata.org/dataset/21e997e2-81a9-4425-be59-3436641c55d1/resource/fa348275-17ee-45a2-8f1e-845e010a054a/download/eadw-cdi-data-2025-07-01.tif
  format: null
  id: resource_fa348275
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: eadw-cdi-data-2025-07-01.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: IGAD Region - Dekadal Combined Drought Indicator (CDI) 2025 (Dekadal
    (10 days) Combined Drought Indicator (CDI) for 2025-07-11)
  download_url: https://data.humdata.org/dataset/21e997e2-81a9-4425-be59-3436641c55d1/resource/47f42cad-d91e-4ebc-b0aa-3479c5342328/download/eadw-cdi-data-2025-07-11.tif
  format: null
  id: resource_47f42cad
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: eadw-cdi-data-2025-07-11.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: IGAD Region - Dekadal Combined Drought Indicator (CDI) 2025 (Dekadal
    (10 days) Combined Drought Indicator (CDI) for 2025-07-21)
  download_url: https://data.humdata.org/dataset/21e997e2-81a9-4425-be59-3436641c55d1/resource/e0eb2e1a-4506-458e-a571-8e110761822e/download/eadw-cdi-data-2025-07-21.tif
  format: null
  id: resource_e0eb2e1a
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: eadw-cdi-data-2025-07-21.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: IGAD Region - Dekadal Combined Drought Indicator (CDI) 2025 (Dekadal
    (10 days) Combined Drought Indicator (CDI) for 2025-08-01)
  download_url: https://data.humdata.org/dataset/21e997e2-81a9-4425-be59-3436641c55d1/resource/6fb26e7f-c4a5-400a-8e86-c6deb41653da/download/eadw-cdi-data-2025-08-01.tif
  format: null
  id: resource_6fb26e7f
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: eadw-cdi-data-2025-08-01.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: IGAD Region - Dekadal Combined Drought Indicator (CDI) 2025 (Dekadal
    (10 days) Combined Drought Indicator (CDI) for 2025-08-11)
  download_url: https://data.humdata.org/dataset/21e997e2-81a9-4425-be59-3436641c55d1/resource/f1ef365e-535a-416b-a6a9-3a599659857a/download/eadw-cdi-data-2025-08-11.tif
  format: null
  id: resource_f1ef365e
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: eadw-cdi-data-2025-08-11.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: IGAD Region - Dekadal Combined Drought Indicator (CDI) 2025 (Dekadal
    (10 days) Combined Drought Indicator (CDI) for 2025-08-21)
  download_url: https://data.humdata.org/dataset/21e997e2-81a9-4425-be59-3436641c55d1/resource/d7d3c4a7-ff27-48b8-8e55-7ee1b8a53f82/download/eadw-cdi-data-2025-08-21.tif
  format: null
  id: resource_d7d3c4a7
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: eadw-cdi-data-2025-08-21.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: IGAD Region - Dekadal Combined Drought Indicator (CDI) 2025 (Dekadal
    (10 days) Combined Drought Indicator (CDI) for 2025-09-01)
  download_url: https://data.humdata.org/dataset/21e997e2-81a9-4425-be59-3436641c55d1/resource/85b1526c-ea35-4d22-be7a-ff69261d8158/download/eadw-cdi-data-2025-09-01.tif
  format: null
  id: resource_85b1526c
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: eadw-cdi-data-2025-09-01.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: IGAD Region - Dekadal Combined Drought Indicator (CDI) 2025 (Dekadal
    (10 days) Combined Drought Indicator (CDI) for 2025-09-11)
  download_url: https://data.humdata.org/dataset/21e997e2-81a9-4425-be59-3436641c55d1/resource/8bf769e9-fc5c-420a-a3db-6770231cd0c1/download/eadw-cdi-data-2025-09-11.tif
  format: null
  id: resource_8bf769e9
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: eadw-cdi-data-2025-09-11.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: IGAD Region - Dekadal Combined Drought Indicator (CDI) 2025 (Dekadal
    (10 days) Combined Drought Indicator (CDI) for 2025-09-21)
  download_url: https://data.humdata.org/dataset/21e997e2-81a9-4425-be59-3436641c55d1/resource/52c13173-a963-4319-9823-5f7993744fe5/download/eadw-cdi-data-2025-09-21.tif
  format: null
  id: resource_52c13173
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: eadw-cdi-data-2025-09-21.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: IGAD Region - Dekadal Combined Drought Indicator (CDI) 2025 (Dekadal
    (10 days) Combined Drought Indicator (CDI) for 2025-10-01)
  download_url: https://data.humdata.org/dataset/21e997e2-81a9-4425-be59-3436641c55d1/resource/6786f13a-0c7c-48ba-8055-6fef0162a062/download/eadw-cdi-data-2025-10-01.tif
  format: null
  id: resource_6786f13a
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: eadw-cdi-data-2025-10-01.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: IGAD Region - Dekadal Combined Drought Indicator (CDI) 2025 (Dekadal
    (10 days) Combined Drought Indicator (CDI) for 2025-10-11)
  download_url: https://data.humdata.org/dataset/21e997e2-81a9-4425-be59-3436641c55d1/resource/5cdf35c3-dee9-48be-b7a7-eaa17f97098b/download/eadw-cdi-data-2025-10-11.tif
  format: null
  id: resource_5cdf35c3
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: eadw-cdi-data-2025-10-11.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: IGAD Region - Dekadal Combined Drought Indicator (CDI) 2025 (Dekadal
    (10 days) Combined Drought Indicator (CDI) for 2025-10-21)
  download_url: https://data.humdata.org/dataset/21e997e2-81a9-4425-be59-3436641c55d1/resource/7c4c7f1d-3276-44d5-91c8-0df6cb53968b/download/eadw-cdi-data-2025-10-21.tif
  format: null
  id: resource_7c4c7f1d
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: eadw-cdi-data-2025-10-21.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: IGAD Region - Dekadal Combined Drought Indicator (CDI) 2025 (Dekadal
    (10 days) Combined Drought Indicator (CDI) for 2025-11-01)
  download_url: https://data.humdata.org/dataset/21e997e2-81a9-4425-be59-3436641c55d1/resource/d307af9c-e928-4f05-a900-5853e11989d1/download/eadw-cdi-data-2025-11-01.tif
  format: null
  id: resource_d307af9c
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: eadw-cdi-data-2025-11-01.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: IGAD Region - Dekadal Combined Drought Indicator (CDI) 2025 (Dekadal
    (10 days) Combined Drought Indicator (CDI) for 2025-11-11)
  download_url: https://data.humdata.org/dataset/21e997e2-81a9-4425-be59-3436641c55d1/resource/0bf6ea08-41b8-4eb7-bc8c-4342a16d1b76/download/eadw-cdi-data-2025-11-11.tif
  format: null
  id: resource_0bf6ea08
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: eadw-cdi-data-2025-11-11.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: IGAD Region - Dekadal Combined Drought Indicator (CDI) 2025 (Dekadal
    (10 days) Combined Drought Indicator (CDI) for 2025-11-21)
  download_url: https://data.humdata.org/dataset/21e997e2-81a9-4425-be59-3436641c55d1/resource/e50fa573-38a3-4a8f-a7fa-b5a618a23e5b/download/eadw-cdi-data-2025-11-21.tif
  format: null
  id: resource_e50fa573
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: eadw-cdi-data-2025-11-21.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: IGAD Region - Dekadal Combined Drought Indicator (CDI) 2025 (Dekadal
    (10 days) Combined Drought Indicator (CDI) for 2025-12-01)
  download_url: https://data.humdata.org/dataset/21e997e2-81a9-4425-be59-3436641c55d1/resource/6eaa1370-f40a-488c-88eb-57ca5f40c9ad/download/eadw-cdi-data-2025-12-01.tif
  format: null
  id: resource_6eaa1370
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: eadw-cdi-data-2025-12-01.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: IGAD Region - Dekadal Combined Drought Indicator (CDI) 2025 (Dekadal
    (10 days) Combined Drought Indicator (CDI) for 2025-12-11)
  download_url: https://data.humdata.org/dataset/21e997e2-81a9-4425-be59-3436641c55d1/resource/73b9ba3c-8e90-4134-8d70-973ae7d9bcc2/download/eadw-cdi-data-2025-12-11.tif
  format: null
  id: resource_73b9ba3c
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: eadw-cdi-data-2025-12-11.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: IGAD Region - Dekadal Combined Drought Indicator (CDI) 2025 (Dekadal
    (10 days) Combined Drought Indicator (CDI) for 2025-12-21)
  download_url: https://data.humdata.org/dataset/21e997e2-81a9-4425-be59-3436641c55d1/resource/c9c903f4-7ee1-4d6a-b090-31c9692e858c/download/eadw-cdi-data-2025-12-21.tif
  format: null
  id: resource_c9c903f4
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: eadw-cdi-data-2025-12-21.tif
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-icpac_regiondekadalcombineddrou_2025
spatial:
  bbox: null
  centroid: null
  countries:
  - DZA
  - DJI
  - ERI
  - ETH
  - KEN
  - SOM
  - SSD
  - UGA
  gazetteer_entries: []
  scale: regional
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2025-12-30'
  start: '2025-01-01'
temporal_resolution: null
title: IGAD Region - Dekadal Combined Drought Indicator (CDI) 2025
version: null
vulnerability: null
---
