---
attributions:
- entity:
    affiliation: null
    email: null
    name: European Commission, Joint Research Centre (JRC)
    url: https://data.humdata.org/dataset/tca-anomalies-fapar-viirs
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Copernicus
  url: https://data.humdata.org/dataset/tca-anomalies-fapar-viirs
creator:
  affiliation: null
  email: null
  name: Copernicus
  url: https://data.humdata.org/dataset/tca-anomalies-fapar-viirs
dataset_id: rdls_hzd-tca_copernicus_turkscaicosislandsvegetat_2012
description: 'Fraction of Absorbed Photosynthetically Active Radiation (FAPAR) is
  a biophysical dimensionless quantity (its values range from 0/no absorption to 1/total
  absorption) used to assess the greenness and health of vegetation. FAPAR anomalies
  can be used as an indicator to detect and monitor the impacts of agricultural drought
  on the growth and productivity of vegetation. The data is presented in 10-day time
  composite of the Visible Infrared Imaging Radiometer Suite (VIIRS).. [Source: This
  metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/tca-anomalies-fapar-viirs]'
details: Variations in the vegetation health and/or cover could be related to stress
  factors not related to droughts (e.g., plant diseases, pests, hail, flooding). To
  determine if changes in FAPAR are linked with a drought event or not, FAPAR data
  should be interpreted jointly with other indicators (as in the EDO Combined Drought
  Indicator).
exposure: []
hazard:
  event_sets_by_hazard_type:
    drought:
    - analysis_type: empirical
      calculation_method: observed
      event_count: 0
      events: []
      frequency_distribution: null
      hazards:
      - classification: null
        id: hazard_1
        intensity_measure: FAPAR:-
        process: agricultural_drought
        trigger: null
        type: drought
      id: event_set_1
      occurrence_range: null
      seasonality: null
  event_sets_count: 1
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: FAPAR values from VIIRS satellite observations are collected at 10-day
    intervals. Anomalies are calculated by computing the deviation of FAPAR values
    from a long-term mean baseline (2012 to the last available full year) at each
    grid cell. The resulting raster datasets are distributed as GeoTIFF files for
    annual periods spanning 2012-2026.
  sources:
  - id: source_1
    license: null
    name: European Commission, Joint Research Centre (JRC)
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/tca-anomalies-fapar-viirs
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
  url: https://drought.emergency.copernicus.eu/data/factsheets/factsheet_fapar_viirs.pdf
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Turks and Caicos Islands: Copernicus Vegetation Index Anomaly (FAPAR
    Anomaly) (Data from 2026-01-01 to 2026-01-10)'
  download_url: https://data.humdata.org/dataset/489fb281-7560-43fa-8273-a1780a53bd7a/resource/bb261f6b-004f-43bb-8d4d-551f775ab749/download/tca_fpanv_m_gdo_20260101_20260101_t.zip
  format: null
  id: resource_bb261f6b
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: tca_fpanv_m_gdo_20260101_20260101_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Turks and Caicos Islands: Copernicus Vegetation Index Anomaly (FAPAR
    Anomaly) (Data from 2025-01-01 to 2025-12-31)'
  download_url: https://data.humdata.org/dataset/489fb281-7560-43fa-8273-a1780a53bd7a/resource/126f2561-19a3-4c04-a96c-56fc30f41552/download/tca_fpanv_m_gdo_20250101_20251221_t.zip
  format: null
  id: resource_126f2561
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: tca_fpanv_m_gdo_20250101_20251221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Turks and Caicos Islands: Copernicus Vegetation Index Anomaly (FAPAR
    Anomaly) (Data from 2024-01-01 to 2024-12-31)'
  download_url: https://data.humdata.org/dataset/489fb281-7560-43fa-8273-a1780a53bd7a/resource/b66575c6-1ce3-4559-85ee-1ee93ba645fc/download/tca_fpanv_m_gdo_20240101_20241221_t.zip
  format: null
  id: resource_b66575c6
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: tca_fpanv_m_gdo_20240101_20241221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Turks and Caicos Islands: Copernicus Vegetation Index Anomaly (FAPAR
    Anomaly) (Data from 2023-01-01 to 2023-12-31)'
  download_url: https://data.humdata.org/dataset/489fb281-7560-43fa-8273-a1780a53bd7a/resource/7e9eab0e-6623-44a1-97bd-5feca686819e/download/tca_fpanv_m_gdo_20230101_20231221_t.zip
  format: null
  id: resource_7e9eab0e
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: tca_fpanv_m_gdo_20230101_20231221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Turks and Caicos Islands: Copernicus Vegetation Index Anomaly (FAPAR
    Anomaly) (Data from 2022-01-01 to 2022-12-31)'
  download_url: https://data.humdata.org/dataset/489fb281-7560-43fa-8273-a1780a53bd7a/resource/79028096-0654-4b07-b2e6-a6775c8c9c6b/download/tca_fpanv_m_gdo_20220101_20221221_t.zip
  format: null
  id: resource_79028096
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: tca_fpanv_m_gdo_20220101_20221221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Turks and Caicos Islands: Copernicus Vegetation Index Anomaly (FAPAR
    Anomaly) (Data from 2021-01-01 to 2021-12-31)'
  download_url: https://data.humdata.org/dataset/489fb281-7560-43fa-8273-a1780a53bd7a/resource/c2e1c6be-a27a-428e-b9c0-bc51056e390d/download/tca_fpanv_m_gdo_20210101_20211221_t.zip
  format: null
  id: resource_c2e1c6be
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: tca_fpanv_m_gdo_20210101_20211221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Turks and Caicos Islands: Copernicus Vegetation Index Anomaly (FAPAR
    Anomaly) (Data from 2020-01-01 to 2020-12-31)'
  download_url: https://data.humdata.org/dataset/489fb281-7560-43fa-8273-a1780a53bd7a/resource/844ee428-16fd-4600-928a-73cc321161ef/download/tca_fpanv_m_gdo_20200101_20201221_t.zip
  format: null
  id: resource_844ee428
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: tca_fpanv_m_gdo_20200101_20201221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Turks and Caicos Islands: Copernicus Vegetation Index Anomaly (FAPAR
    Anomaly) (Data from 2019-01-01 to 2019-12-31)'
  download_url: https://data.humdata.org/dataset/489fb281-7560-43fa-8273-a1780a53bd7a/resource/4d1a2f0c-cd0d-4f69-bee4-83d61c543432/download/tca_fpanv_m_gdo_20190101_20191221_t.zip
  format: null
  id: resource_4d1a2f0c
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: tca_fpanv_m_gdo_20190101_20191221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Turks and Caicos Islands: Copernicus Vegetation Index Anomaly (FAPAR
    Anomaly) (Data from 2018-01-01 to 2018-12-31)'
  download_url: https://data.humdata.org/dataset/489fb281-7560-43fa-8273-a1780a53bd7a/resource/7e70bcaf-19d9-4dfc-98ba-5312c1a6e14c/download/tca_fpanv_m_gdo_20180101_20181221_t.zip
  format: null
  id: resource_7e70bcaf
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: tca_fpanv_m_gdo_20180101_20181221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Turks and Caicos Islands: Copernicus Vegetation Index Anomaly (FAPAR
    Anomaly) (Data from 2017-01-01 to 2017-12-31)'
  download_url: https://data.humdata.org/dataset/489fb281-7560-43fa-8273-a1780a53bd7a/resource/02e1d771-4e1c-4c72-ab45-be36f7845c98/download/tca_fpanv_m_gdo_20170101_20171221_t.zip
  format: null
  id: resource_02e1d771
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: tca_fpanv_m_gdo_20170101_20171221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Turks and Caicos Islands: Copernicus Vegetation Index Anomaly (FAPAR
    Anomaly) (Data from 2016-01-01 to 2016-12-31)'
  download_url: https://data.humdata.org/dataset/489fb281-7560-43fa-8273-a1780a53bd7a/resource/3ecfa636-57d0-4116-9fd7-b8a9d7e76d6e/download/tca_fpanv_m_gdo_20160101_20161221_t.zip
  format: null
  id: resource_3ecfa636
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: tca_fpanv_m_gdo_20160101_20161221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Turks and Caicos Islands: Copernicus Vegetation Index Anomaly (FAPAR
    Anomaly) (Data from 2015-01-01 to 2015-12-31)'
  download_url: https://data.humdata.org/dataset/489fb281-7560-43fa-8273-a1780a53bd7a/resource/ca8e5c47-2634-4b7e-99f5-2d42e4a811f5/download/tca_fpanv_m_gdo_20150101_20151221_t.zip
  format: null
  id: resource_ca8e5c47
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: tca_fpanv_m_gdo_20150101_20151221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Turks and Caicos Islands: Copernicus Vegetation Index Anomaly (FAPAR
    Anomaly) (Data from 2014-01-01 to 2014-12-31)'
  download_url: https://data.humdata.org/dataset/489fb281-7560-43fa-8273-a1780a53bd7a/resource/02629089-7bd6-4f87-8ffd-2e945a1a69af/download/tca_fpanv_m_gdo_20140101_20141221_t.zip
  format: null
  id: resource_02629089
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: tca_fpanv_m_gdo_20140101_20141221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Turks and Caicos Islands: Copernicus Vegetation Index Anomaly (FAPAR
    Anomaly) (Data from 2013-01-01 to 2013-12-31)'
  download_url: https://data.humdata.org/dataset/489fb281-7560-43fa-8273-a1780a53bd7a/resource/81866d27-b6f3-4987-b748-b56d48187224/download/tca_fpanv_m_gdo_20130101_20131221_t.zip
  format: null
  id: resource_81866d27
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: tca_fpanv_m_gdo_20130101_20131221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Turks and Caicos Islands: Copernicus Vegetation Index Anomaly (FAPAR
    Anomaly) (Data from 2012-01-21 to 2012-12-31)'
  download_url: https://data.humdata.org/dataset/489fb281-7560-43fa-8273-a1780a53bd7a/resource/8e70fd74-b7e4-48bd-8df3-826b9517f0b8/download/tca_fpanv_m_gdo_20120121_20121221_t.zip
  format: null
  id: resource_8e70fd74
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: tca_fpanv_m_gdo_20120121_20121221_t.zip
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-tca_copernicus_turkscaicosislandsvegetat_2012
spatial:
  bbox: null
  centroid: null
  countries:
  - TCA
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2026-01-10'
  start: '2012-01-21'
temporal_resolution: null
title: 'Turks and Caicos Islands: Copernicus Vegetation Index Anomaly (FAPAR Anomaly)'
version: null
vulnerability: null
---
