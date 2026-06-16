---
attributions:
- entity:
    affiliation: null
    email: null
    name: Copernicus / European Commission Joint Research Centre (JRC)
    url: https://data.humdata.org/dataset/ncl-anomalies-fapar-viirs
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Copernicus
  url: https://data.humdata.org/dataset/ncl-anomalies-fapar-viirs
creator:
  affiliation: null
  email: null
  name: Copernicus
  url: https://data.humdata.org/dataset/ncl-anomalies-fapar-viirs
dataset_id: rdls_hzd-ncl_copernicus_newcaledoniavegetationind_2012
description: 'Fraction of Absorbed Photosynthetically Active Radiation (FAPAR) is
  a biophysical dimensionless quantity (its values range from 0/no absorption to 1/total
  absorption) used to assess the greenness and health of vegetation. FAPAR anomalies
  can be used as an indicator to detect and monitor the impacts of agricultural drought
  on the growth and productivity of vegetation. The data is presented in 10-day time
  composite of the Visible Infrared Imaging Radiometer Suite (VIIRS).. [Source: This
  metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/ncl-anomalies-fapar-viirs]'
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
  description: FAPAR values from VIIRS satellite imagery are composited at 10-day
    intervals and processed to calculate anomalies by computing the deviation of each
    grid cell from its long-term mean (baseline 2012 to last complete year). The resulting
    raster anomaly datasets serve as an empirical indicator of agricultural drought
    stress on vegetation across New Caledonia.
  sources:
  - id: source_1
    license: null
    name: Copernicus / European Commission Joint Research Centre (JRC)
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/ncl-anomalies-fapar-viirs
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
  description: 'New Caledonia: Copernicus Vegetation Index Anomaly (FAPAR Anomaly)
    (Data from 2026-01-01 to 2026-01-10)'
  download_url: https://data.humdata.org/dataset/4ee3f85e-9c6d-45b7-867f-48a3c877c5cd/resource/b1ad8de3-6dbd-4f32-8aa2-96e1a8754690/download/ncl_fpanv_m_gdo_20260101_20260101_t.zip
  format: null
  id: resource_b1ad8de3
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ncl_fpanv_m_gdo_20260101_20260101_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'New Caledonia: Copernicus Vegetation Index Anomaly (FAPAR Anomaly)
    (Data from 2025-01-01 to 2025-12-31)'
  download_url: https://data.humdata.org/dataset/4ee3f85e-9c6d-45b7-867f-48a3c877c5cd/resource/7a042c5e-cbaa-4100-87c1-e0438f1fbf9c/download/ncl_fpanv_m_gdo_20250101_20251221_t.zip
  format: null
  id: resource_7a042c5e
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ncl_fpanv_m_gdo_20250101_20251221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'New Caledonia: Copernicus Vegetation Index Anomaly (FAPAR Anomaly)
    (Data from 2024-01-01 to 2024-12-31)'
  download_url: https://data.humdata.org/dataset/4ee3f85e-9c6d-45b7-867f-48a3c877c5cd/resource/2df3a532-a40d-43c5-affb-38701fa4474e/download/ncl_fpanv_m_gdo_20240101_20241221_t.zip
  format: null
  id: resource_2df3a532
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ncl_fpanv_m_gdo_20240101_20241221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'New Caledonia: Copernicus Vegetation Index Anomaly (FAPAR Anomaly)
    (Data from 2023-01-01 to 2023-12-31)'
  download_url: https://data.humdata.org/dataset/4ee3f85e-9c6d-45b7-867f-48a3c877c5cd/resource/760fc0b2-62ed-47b2-a56f-eda7a8231c68/download/ncl_fpanv_m_gdo_20230101_20231221_t.zip
  format: null
  id: resource_760fc0b2
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ncl_fpanv_m_gdo_20230101_20231221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'New Caledonia: Copernicus Vegetation Index Anomaly (FAPAR Anomaly)
    (Data from 2022-01-01 to 2022-12-31)'
  download_url: https://data.humdata.org/dataset/4ee3f85e-9c6d-45b7-867f-48a3c877c5cd/resource/05687ceb-bb4e-4163-8404-c2059fc8501f/download/ncl_fpanv_m_gdo_20220101_20221221_t.zip
  format: null
  id: resource_05687ceb
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ncl_fpanv_m_gdo_20220101_20221221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'New Caledonia: Copernicus Vegetation Index Anomaly (FAPAR Anomaly)
    (Data from 2021-01-01 to 2021-12-31)'
  download_url: https://data.humdata.org/dataset/4ee3f85e-9c6d-45b7-867f-48a3c877c5cd/resource/d7b49fd8-2133-4bf9-bb6e-a9fdb872ce2b/download/ncl_fpanv_m_gdo_20210101_20211221_t.zip
  format: null
  id: resource_d7b49fd8
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ncl_fpanv_m_gdo_20210101_20211221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'New Caledonia: Copernicus Vegetation Index Anomaly (FAPAR Anomaly)
    (Data from 2020-01-01 to 2020-12-31)'
  download_url: https://data.humdata.org/dataset/4ee3f85e-9c6d-45b7-867f-48a3c877c5cd/resource/78b38fa3-4065-432a-8b1f-bd76ad122dee/download/ncl_fpanv_m_gdo_20200101_20201221_t.zip
  format: null
  id: resource_78b38fa3
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ncl_fpanv_m_gdo_20200101_20201221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'New Caledonia: Copernicus Vegetation Index Anomaly (FAPAR Anomaly)
    (Data from 2019-01-01 to 2019-12-31)'
  download_url: https://data.humdata.org/dataset/4ee3f85e-9c6d-45b7-867f-48a3c877c5cd/resource/199a2ca1-18f3-4170-82a7-7e8789ff4c85/download/ncl_fpanv_m_gdo_20190101_20191221_t.zip
  format: null
  id: resource_199a2ca1
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ncl_fpanv_m_gdo_20190101_20191221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'New Caledonia: Copernicus Vegetation Index Anomaly (FAPAR Anomaly)
    (Data from 2018-01-01 to 2018-12-31)'
  download_url: https://data.humdata.org/dataset/4ee3f85e-9c6d-45b7-867f-48a3c877c5cd/resource/6dd0fdc2-2373-4bfc-a4f2-67053564a033/download/ncl_fpanv_m_gdo_20180101_20181221_t.zip
  format: null
  id: resource_6dd0fdc2
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ncl_fpanv_m_gdo_20180101_20181221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'New Caledonia: Copernicus Vegetation Index Anomaly (FAPAR Anomaly)
    (Data from 2017-01-01 to 2017-12-31)'
  download_url: https://data.humdata.org/dataset/4ee3f85e-9c6d-45b7-867f-48a3c877c5cd/resource/6499e73f-6ba3-4c2f-91d4-5534c50dbd5b/download/ncl_fpanv_m_gdo_20170101_20171221_t.zip
  format: null
  id: resource_6499e73f
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ncl_fpanv_m_gdo_20170101_20171221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'New Caledonia: Copernicus Vegetation Index Anomaly (FAPAR Anomaly)
    (Data from 2016-01-01 to 2016-12-31)'
  download_url: https://data.humdata.org/dataset/4ee3f85e-9c6d-45b7-867f-48a3c877c5cd/resource/77e99039-d9b2-4436-9a28-4a2c0475f6bf/download/ncl_fpanv_m_gdo_20160101_20161221_t.zip
  format: null
  id: resource_77e99039
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ncl_fpanv_m_gdo_20160101_20161221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'New Caledonia: Copernicus Vegetation Index Anomaly (FAPAR Anomaly)
    (Data from 2015-01-01 to 2015-12-31)'
  download_url: https://data.humdata.org/dataset/4ee3f85e-9c6d-45b7-867f-48a3c877c5cd/resource/70021b6d-b2dd-4a89-850f-f5fe21d5a78a/download/ncl_fpanv_m_gdo_20150101_20151221_t.zip
  format: null
  id: resource_70021b6d
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ncl_fpanv_m_gdo_20150101_20151221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'New Caledonia: Copernicus Vegetation Index Anomaly (FAPAR Anomaly)
    (Data from 2014-01-01 to 2014-12-31)'
  download_url: https://data.humdata.org/dataset/4ee3f85e-9c6d-45b7-867f-48a3c877c5cd/resource/22bc73ad-935c-4a80-b405-8608f5fbf3b7/download/ncl_fpanv_m_gdo_20140101_20141221_t.zip
  format: null
  id: resource_22bc73ad
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ncl_fpanv_m_gdo_20140101_20141221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'New Caledonia: Copernicus Vegetation Index Anomaly (FAPAR Anomaly)
    (Data from 2013-01-01 to 2013-12-31)'
  download_url: https://data.humdata.org/dataset/4ee3f85e-9c6d-45b7-867f-48a3c877c5cd/resource/6c4999b2-ee50-420c-bd10-7ccbe5d7dc92/download/ncl_fpanv_m_gdo_20130101_20131221_t.zip
  format: null
  id: resource_6c4999b2
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ncl_fpanv_m_gdo_20130101_20131221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'New Caledonia: Copernicus Vegetation Index Anomaly (FAPAR Anomaly)
    (Data from 2012-01-21 to 2012-12-31)'
  download_url: https://data.humdata.org/dataset/4ee3f85e-9c6d-45b7-867f-48a3c877c5cd/resource/8fe31a89-03a3-4fdd-8635-7eb6ada4426b/download/ncl_fpanv_m_gdo_20120121_20121221_t.zip
  format: null
  id: resource_8fe31a89
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ncl_fpanv_m_gdo_20120121_20121221_t.zip
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-ncl_copernicus_newcaledoniavegetationind_2012
spatial:
  bbox: null
  centroid: null
  countries:
  - NCL
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2026-01-10'
  start: '2012-01-21'
temporal_resolution: null
title: 'New Caledonia: Copernicus Vegetation Index Anomaly (FAPAR Anomaly)'
version: null
vulnerability: null
---
