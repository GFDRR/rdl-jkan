---
attributions:
- entity:
    affiliation: null
    email: null
    name: European Commission, Joint Research Centre (JRC)
    url: https://data.humdata.org/dataset/fsm-anomalies-fapar-viirs
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Copernicus
  url: https://data.humdata.org/dataset/fsm-anomalies-fapar-viirs
creator:
  affiliation: null
  email: null
  name: Copernicus
  url: https://data.humdata.org/dataset/fsm-anomalies-fapar-viirs
dataset_id: rdls_hzd-fsm_copernicus_micronesiafederatedstates_2012
description: 'Fraction of Absorbed Photosynthetically Active Radiation (FAPAR) is
  a biophysical dimensionless quantity (its values range from 0/no absorption to 1/total
  absorption) used to assess the greenness and health of vegetation. FAPAR anomalies
  can be used as an indicator to detect and monitor the impacts of agricultural drought
  on the growth and productivity of vegetation. The data is presented in 10-day time
  composite of the Visible Infrared Imaging Radiometer Suite (VIIRS).. [Source: This
  metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/fsm-anomalies-fapar-viirs]'
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
  type: drought
license: CC-BY-4.0
lineage:
  description: FAPAR values from VIIRS satellite observations are collected at 10-day
    intervals and processed into raster composites. Anomalies are calculated by computing
    the deviation of each grid cell's FAPAR value from its long-term mean baseline
    (2012 to the last available full year), enabling detection and monitoring of agricultural
    drought impacts on vegetation productivity across Micronesia.
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
- href: https://data.humdata.org/dataset/fsm-anomalies-fapar-viirs
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
  description: 'Micronesia (Federated States of): Copernicus Vegetation Index Anomaly
    (FAPAR Anomaly) (Data from 2026-01-01 to 2026-01-10)'
  download_url: https://data.humdata.org/dataset/15d4b936-cd7f-43f4-aec2-a1422dbea1c2/resource/4606a694-7848-4230-86a8-3c07c3087f10/download/fsm_fpanv_m_gdo_20260101_20260101_t.zip
  format: null
  id: resource_4606a694
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: fsm_fpanv_m_gdo_20260101_20260101_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Micronesia (Federated States of): Copernicus Vegetation Index Anomaly
    (FAPAR Anomaly) (Data from 2025-01-01 to 2025-12-31)'
  download_url: https://data.humdata.org/dataset/15d4b936-cd7f-43f4-aec2-a1422dbea1c2/resource/58af39b6-8ffe-4b4e-8dd8-886017ac1690/download/fsm_fpanv_m_gdo_20250101_20251221_t.zip
  format: null
  id: resource_58af39b6
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: fsm_fpanv_m_gdo_20250101_20251221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Micronesia (Federated States of): Copernicus Vegetation Index Anomaly
    (FAPAR Anomaly) (Data from 2024-01-01 to 2024-12-31)'
  download_url: https://data.humdata.org/dataset/15d4b936-cd7f-43f4-aec2-a1422dbea1c2/resource/fbe04559-d6e2-4c30-8975-3fc38b0b013e/download/fsm_fpanv_m_gdo_20240101_20241221_t.zip
  format: null
  id: resource_fbe04559
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: fsm_fpanv_m_gdo_20240101_20241221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Micronesia (Federated States of): Copernicus Vegetation Index Anomaly
    (FAPAR Anomaly) (Data from 2023-01-01 to 2023-12-31)'
  download_url: https://data.humdata.org/dataset/15d4b936-cd7f-43f4-aec2-a1422dbea1c2/resource/186ff9fc-9b72-4a3c-a6ef-f3d8ea30a15d/download/fsm_fpanv_m_gdo_20230101_20231221_t.zip
  format: null
  id: resource_186ff9fc
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: fsm_fpanv_m_gdo_20230101_20231221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Micronesia (Federated States of): Copernicus Vegetation Index Anomaly
    (FAPAR Anomaly) (Data from 2022-01-01 to 2022-12-31)'
  download_url: https://data.humdata.org/dataset/15d4b936-cd7f-43f4-aec2-a1422dbea1c2/resource/15b77699-e9d2-4cd1-bcb5-6688dcbeee3a/download/fsm_fpanv_m_gdo_20220101_20221221_t.zip
  format: null
  id: resource_15b77699
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: fsm_fpanv_m_gdo_20220101_20221221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Micronesia (Federated States of): Copernicus Vegetation Index Anomaly
    (FAPAR Anomaly) (Data from 2021-01-01 to 2021-12-31)'
  download_url: https://data.humdata.org/dataset/15d4b936-cd7f-43f4-aec2-a1422dbea1c2/resource/cca3228d-5cc4-4324-94a4-48ebce774a6c/download/fsm_fpanv_m_gdo_20210101_20211221_t.zip
  format: null
  id: resource_cca3228d
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: fsm_fpanv_m_gdo_20210101_20211221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Micronesia (Federated States of): Copernicus Vegetation Index Anomaly
    (FAPAR Anomaly) (Data from 2020-01-01 to 2020-12-31)'
  download_url: https://data.humdata.org/dataset/15d4b936-cd7f-43f4-aec2-a1422dbea1c2/resource/d783e1e4-39cf-4c0e-a4e5-e9597baf5b7e/download/fsm_fpanv_m_gdo_20200101_20201221_t.zip
  format: null
  id: resource_d783e1e4
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: fsm_fpanv_m_gdo_20200101_20201221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Micronesia (Federated States of): Copernicus Vegetation Index Anomaly
    (FAPAR Anomaly) (Data from 2019-01-01 to 2019-12-31)'
  download_url: https://data.humdata.org/dataset/15d4b936-cd7f-43f4-aec2-a1422dbea1c2/resource/7ab55b6a-6a0a-4af0-b51e-55330fc7e5ba/download/fsm_fpanv_m_gdo_20190101_20191221_t.zip
  format: null
  id: resource_7ab55b6a
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: fsm_fpanv_m_gdo_20190101_20191221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Micronesia (Federated States of): Copernicus Vegetation Index Anomaly
    (FAPAR Anomaly) (Data from 2018-01-01 to 2018-12-31)'
  download_url: https://data.humdata.org/dataset/15d4b936-cd7f-43f4-aec2-a1422dbea1c2/resource/2f34b582-eaef-4a38-b892-bfcec65fc81e/download/fsm_fpanv_m_gdo_20180101_20181221_t.zip
  format: null
  id: resource_2f34b582
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: fsm_fpanv_m_gdo_20180101_20181221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Micronesia (Federated States of): Copernicus Vegetation Index Anomaly
    (FAPAR Anomaly) (Data from 2017-01-01 to 2017-12-31)'
  download_url: https://data.humdata.org/dataset/15d4b936-cd7f-43f4-aec2-a1422dbea1c2/resource/4225c0e6-3ce4-405c-86bb-607cba4e75c5/download/fsm_fpanv_m_gdo_20170101_20171221_t.zip
  format: null
  id: resource_4225c0e6
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: fsm_fpanv_m_gdo_20170101_20171221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Micronesia (Federated States of): Copernicus Vegetation Index Anomaly
    (FAPAR Anomaly) (Data from 2016-01-01 to 2016-12-31)'
  download_url: https://data.humdata.org/dataset/15d4b936-cd7f-43f4-aec2-a1422dbea1c2/resource/62a1f799-1122-4c71-b068-a529fd1101b2/download/fsm_fpanv_m_gdo_20160101_20161221_t.zip
  format: null
  id: resource_62a1f799
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: fsm_fpanv_m_gdo_20160101_20161221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Micronesia (Federated States of): Copernicus Vegetation Index Anomaly
    (FAPAR Anomaly) (Data from 2015-01-01 to 2015-12-31)'
  download_url: https://data.humdata.org/dataset/15d4b936-cd7f-43f4-aec2-a1422dbea1c2/resource/33333c53-b421-44d3-b38d-4d8d357f76dd/download/fsm_fpanv_m_gdo_20150101_20151221_t.zip
  format: null
  id: resource_33333c53
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: fsm_fpanv_m_gdo_20150101_20151221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Micronesia (Federated States of): Copernicus Vegetation Index Anomaly
    (FAPAR Anomaly) (Data from 2014-01-01 to 2014-12-31)'
  download_url: https://data.humdata.org/dataset/15d4b936-cd7f-43f4-aec2-a1422dbea1c2/resource/a8d15a1f-72e9-41b0-bad3-887e390d0227/download/fsm_fpanv_m_gdo_20140101_20141221_t.zip
  format: null
  id: resource_a8d15a1f
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: fsm_fpanv_m_gdo_20140101_20141221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Micronesia (Federated States of): Copernicus Vegetation Index Anomaly
    (FAPAR Anomaly) (Data from 2013-01-01 to 2013-12-31)'
  download_url: https://data.humdata.org/dataset/15d4b936-cd7f-43f4-aec2-a1422dbea1c2/resource/a489577e-0fee-4a49-a826-03ba336a9b52/download/fsm_fpanv_m_gdo_20130101_20131221_t.zip
  format: null
  id: resource_a489577e
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: fsm_fpanv_m_gdo_20130101_20131221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Micronesia (Federated States of): Copernicus Vegetation Index Anomaly
    (FAPAR Anomaly) (Data from 2012-01-21 to 2012-12-31)'
  download_url: https://data.humdata.org/dataset/15d4b936-cd7f-43f4-aec2-a1422dbea1c2/resource/3f8f93f2-346f-441b-893c-bc1f3191d3e0/download/fsm_fpanv_m_gdo_20120121_20121221_t.zip
  format: null
  id: resource_3f8f93f2
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: fsm_fpanv_m_gdo_20120121_20121221_t.zip
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-fsm_copernicus_micronesiafederatedstates_2012
spatial:
  bbox: null
  centroid: null
  countries:
  - FSM
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2026-01-10'
  start: '2012-01-21'
temporal_resolution: null
title: 'Micronesia (Federated States of): Copernicus Vegetation Index Anomaly (FAPAR
  Anomaly)'
version: null
vulnerability: null
---
