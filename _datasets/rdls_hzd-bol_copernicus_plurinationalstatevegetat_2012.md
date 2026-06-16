---
attributions:
- entity:
    affiliation: null
    email: null
    name: European Commission, Joint Research Centre (JRC)
    url: https://data.humdata.org/dataset/bol-anomalies-fapar-viirs
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Copernicus
  url: https://data.humdata.org/dataset/bol-anomalies-fapar-viirs
creator:
  affiliation: null
  email: null
  name: Copernicus
  url: https://data.humdata.org/dataset/bol-anomalies-fapar-viirs
dataset_id: rdls_hzd-bol_copernicus_plurinationalstatevegetat_2012
description: 'Fraction of Absorbed Photosynthetically Active Radiation (FAPAR) is
  a biophysical dimensionless quantity (its values range from 0/no absorption to 1/total
  absorption) used to assess the greenness and health of vegetation. FAPAR anomalies
  can be used as an indicator to detect and monitor the impacts of agricultural drought
  on the growth and productivity of vegetation. The data is presented in 10-day time
  composite of the Visible Infrared Imaging Radiometer Suite (VIIRS).. [Source: This
  metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/bol-anomalies-fapar-viirs]'
details: Variations in the vegetation health and/or cover could be related to stress
  factors not related to droughts (e.g., plant diseases, pests, hail, flooding). To
  determine if changes in FAPAR are linked with a drought event or not, FAPAR data
  should be interpreted jointly with other indicators (as in the EDO Combined Drought
  Indicator).
exposure: []
hazard:
  event_sets:
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
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: FAPAR values from VIIRS satellite observations are collected at 10-day
    intervals and processed into raster composites. Anomalies are calculated by computing
    the deviation of each grid cell's FAPAR value from its long-term mean baseline
    (2012 to the last available full year), enabling detection and monitoring of agricultural
    drought impacts on vegetation productivity across Bolivia.
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
- href: https://data.humdata.org/dataset/bol-anomalies-fapar-viirs
  rel: source
loss: null
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
  description: 'Bolivia (Plurinational State of): Copernicus Vegetation Index Anomaly
    (FAPAR Anomaly) (Data from 2026-01-01 to 2026-01-10)'
  download_url: https://data.humdata.org/dataset/e319f856-e3ca-4a8c-87fa-2f5f7141d8fc/resource/29467f57-a6cd-4df5-81bd-e2f1814231be/download/bol_fpanv_m_gdo_20260101_20260101_t.zip
  format: null
  id: resource_29467f57
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bol_fpanv_m_gdo_20260101_20260101_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Bolivia (Plurinational State of): Copernicus Vegetation Index Anomaly
    (FAPAR Anomaly) (Data from 2025-01-01 to 2025-12-31)'
  download_url: https://data.humdata.org/dataset/e319f856-e3ca-4a8c-87fa-2f5f7141d8fc/resource/8d39cdd2-cb0e-4c57-9008-dac69e9c0477/download/bol_fpanv_m_gdo_20250101_20251221_t.zip
  format: null
  id: resource_8d39cdd2
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bol_fpanv_m_gdo_20250101_20251221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Bolivia (Plurinational State of): Copernicus Vegetation Index Anomaly
    (FAPAR Anomaly) (Data from 2024-01-01 to 2024-12-31)'
  download_url: https://data.humdata.org/dataset/e319f856-e3ca-4a8c-87fa-2f5f7141d8fc/resource/2e55b034-dea8-4d1f-a983-8f5544da84e9/download/bol_fpanv_m_gdo_20240101_20241221_t.zip
  format: null
  id: resource_2e55b034
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bol_fpanv_m_gdo_20240101_20241221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Bolivia (Plurinational State of): Copernicus Vegetation Index Anomaly
    (FAPAR Anomaly) (Data from 2023-01-01 to 2023-12-31)'
  download_url: https://data.humdata.org/dataset/e319f856-e3ca-4a8c-87fa-2f5f7141d8fc/resource/8a203e32-fde7-4fac-bf70-a0ff4f8079ff/download/bol_fpanv_m_gdo_20230101_20231221_t.zip
  format: null
  id: resource_8a203e32
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bol_fpanv_m_gdo_20230101_20231221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Bolivia (Plurinational State of): Copernicus Vegetation Index Anomaly
    (FAPAR Anomaly) (Data from 2022-01-01 to 2022-12-31)'
  download_url: https://data.humdata.org/dataset/e319f856-e3ca-4a8c-87fa-2f5f7141d8fc/resource/e86f4362-3bb1-4459-90a6-f7f9f6c78b78/download/bol_fpanv_m_gdo_20220101_20221221_t.zip
  format: null
  id: resource_e86f4362
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bol_fpanv_m_gdo_20220101_20221221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Bolivia (Plurinational State of): Copernicus Vegetation Index Anomaly
    (FAPAR Anomaly) (Data from 2021-01-01 to 2021-12-31)'
  download_url: https://data.humdata.org/dataset/e319f856-e3ca-4a8c-87fa-2f5f7141d8fc/resource/69c2240d-99c7-4fbd-9c60-6d1e95c9c579/download/bol_fpanv_m_gdo_20210101_20211221_t.zip
  format: null
  id: resource_69c2240d
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bol_fpanv_m_gdo_20210101_20211221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Bolivia (Plurinational State of): Copernicus Vegetation Index Anomaly
    (FAPAR Anomaly) (Data from 2020-01-01 to 2020-12-31)'
  download_url: https://data.humdata.org/dataset/e319f856-e3ca-4a8c-87fa-2f5f7141d8fc/resource/5f86de00-83e4-41ac-b43a-5fed4bb90287/download/bol_fpanv_m_gdo_20200101_20201221_t.zip
  format: null
  id: resource_5f86de00
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bol_fpanv_m_gdo_20200101_20201221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Bolivia (Plurinational State of): Copernicus Vegetation Index Anomaly
    (FAPAR Anomaly) (Data from 2019-01-01 to 2019-12-31)'
  download_url: https://data.humdata.org/dataset/e319f856-e3ca-4a8c-87fa-2f5f7141d8fc/resource/505fd1a5-70ea-4094-a322-a2be1bf45590/download/bol_fpanv_m_gdo_20190101_20191221_t.zip
  format: null
  id: resource_505fd1a5
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bol_fpanv_m_gdo_20190101_20191221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Bolivia (Plurinational State of): Copernicus Vegetation Index Anomaly
    (FAPAR Anomaly) (Data from 2018-01-01 to 2018-12-31)'
  download_url: https://data.humdata.org/dataset/e319f856-e3ca-4a8c-87fa-2f5f7141d8fc/resource/4488ff7b-e602-4ccf-b29a-af6da8207b41/download/bol_fpanv_m_gdo_20180101_20181221_t.zip
  format: null
  id: resource_4488ff7b
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bol_fpanv_m_gdo_20180101_20181221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Bolivia (Plurinational State of): Copernicus Vegetation Index Anomaly
    (FAPAR Anomaly) (Data from 2017-01-01 to 2017-12-31)'
  download_url: https://data.humdata.org/dataset/e319f856-e3ca-4a8c-87fa-2f5f7141d8fc/resource/fec7dc6d-628d-438b-99b3-a11ff99179da/download/bol_fpanv_m_gdo_20170101_20171221_t.zip
  format: null
  id: resource_fec7dc6d
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bol_fpanv_m_gdo_20170101_20171221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Bolivia (Plurinational State of): Copernicus Vegetation Index Anomaly
    (FAPAR Anomaly) (Data from 2016-01-01 to 2016-12-31)'
  download_url: https://data.humdata.org/dataset/e319f856-e3ca-4a8c-87fa-2f5f7141d8fc/resource/72fa44ef-574f-4811-9552-855963ee2ef7/download/bol_fpanv_m_gdo_20160101_20161221_t.zip
  format: null
  id: resource_72fa44ef
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bol_fpanv_m_gdo_20160101_20161221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Bolivia (Plurinational State of): Copernicus Vegetation Index Anomaly
    (FAPAR Anomaly) (Data from 2015-01-01 to 2015-12-31)'
  download_url: https://data.humdata.org/dataset/e319f856-e3ca-4a8c-87fa-2f5f7141d8fc/resource/c95ddd98-1b7b-423a-89dc-295b270e523a/download/bol_fpanv_m_gdo_20150101_20151221_t.zip
  format: null
  id: resource_c95ddd98
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bol_fpanv_m_gdo_20150101_20151221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Bolivia (Plurinational State of): Copernicus Vegetation Index Anomaly
    (FAPAR Anomaly) (Data from 2014-01-01 to 2014-12-31)'
  download_url: https://data.humdata.org/dataset/e319f856-e3ca-4a8c-87fa-2f5f7141d8fc/resource/e12e309f-973f-40d8-99f7-6eab9db8a7a6/download/bol_fpanv_m_gdo_20140101_20141221_t.zip
  format: null
  id: resource_e12e309f
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bol_fpanv_m_gdo_20140101_20141221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Bolivia (Plurinational State of): Copernicus Vegetation Index Anomaly
    (FAPAR Anomaly) (Data from 2013-01-01 to 2013-12-31)'
  download_url: https://data.humdata.org/dataset/e319f856-e3ca-4a8c-87fa-2f5f7141d8fc/resource/3af9377d-337d-4fd3-8fec-e8f3f6c65db2/download/bol_fpanv_m_gdo_20130101_20131221_t.zip
  format: null
  id: resource_3af9377d
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bol_fpanv_m_gdo_20130101_20131221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Bolivia (Plurinational State of): Copernicus Vegetation Index Anomaly
    (FAPAR Anomaly) (Data from 2012-01-21 to 2012-12-31)'
  download_url: https://data.humdata.org/dataset/e319f856-e3ca-4a8c-87fa-2f5f7141d8fc/resource/1df1652d-c15f-4a4b-91f0-80f953105cb4/download/bol_fpanv_m_gdo_20120121_20121221_t.zip
  format: null
  id: resource_1df1652d
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bol_fpanv_m_gdo_20120121_20121221_t.zip
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-bol_copernicus_plurinationalstatevegetat_2012
spatial:
  bbox: null
  centroid: null
  countries:
  - BOL
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2026-01-10'
  start: '2012-01-21'
temporal_resolution: null
title: 'Bolivia (Plurinational State of): Copernicus Vegetation Index Anomaly (FAPAR
  Anomaly)'
version: null
vulnerability: null
---
