---
attributions:
- entity:
    affiliation: null
    email: null
    name: Copernicus / European Commission Joint Research Centre (JRC)
    url: https://data.humdata.org/dataset/atf-anomalies-fapar-viirs
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Copernicus
  url: https://data.humdata.org/dataset/atf-anomalies-fapar-viirs
creator:
  affiliation: null
  email: null
  name: Copernicus
  url: https://data.humdata.org/dataset/atf-anomalies-fapar-viirs
dataset_id: rdls_hzd-atf_copernicus_frenchsouthernterritories_2012
description: 'Fraction of Absorbed Photosynthetically Active Radiation (FAPAR) is
  a biophysical dimensionless quantity (its values range from 0/no absorption to 1/total
  absorption) used to assess the greenness and health of vegetation. FAPAR anomalies
  can be used as an indicator to detect and monitor the impacts of agricultural drought
  on the growth and productivity of vegetation. The data is presented in 10-day time
  composite of the Visible Infrared Imaging Radiometer Suite (VIIRS).. [Source: This
  metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/atf-anomalies-fapar-viirs]'
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
license: CC-BY-4.0
lineage:
  description: FAPAR values from VIIRS satellite observations are collected in 10-day
    time composites. Anomalies are calculated at each grid cell as the deviation from
    a long-term mean baseline (2012 to the last available full year), producing raster
    datasets that serve as an empirical indicator of agricultural drought impacts
    on vegetation.
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
- href: https://data.humdata.org/dataset/atf-anomalies-fapar-viirs
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
  description: 'French Southern Territories: Copernicus Vegetation Index Anomaly (FAPAR
    Anomaly) (Data from 2026-01-01 to 2026-01-10)'
  download_url: https://data.humdata.org/dataset/f4695392-1536-4e15-9616-3bc04dc2f45c/resource/8df7a868-1d5c-4f9d-92db-5af35acc0184/download/atf_fpanv_m_gdo_20260101_20260101_t.zip
  format: null
  id: resource_8df7a868
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: atf_fpanv_m_gdo_20260101_20260101_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'French Southern Territories: Copernicus Vegetation Index Anomaly (FAPAR
    Anomaly) (Data from 2025-01-01 to 2025-12-31)'
  download_url: https://data.humdata.org/dataset/f4695392-1536-4e15-9616-3bc04dc2f45c/resource/3c8aa276-8dbc-444a-8b64-d0f35f3a4a71/download/atf_fpanv_m_gdo_20250101_20251221_t.zip
  format: null
  id: resource_3c8aa276
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: atf_fpanv_m_gdo_20250101_20251221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'French Southern Territories: Copernicus Vegetation Index Anomaly (FAPAR
    Anomaly) (Data from 2024-01-01 to 2024-12-31)'
  download_url: https://data.humdata.org/dataset/f4695392-1536-4e15-9616-3bc04dc2f45c/resource/b8d95706-1d0d-4841-afa4-ddf12098f0bd/download/atf_fpanv_m_gdo_20240101_20241221_t.zip
  format: null
  id: resource_b8d95706
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: atf_fpanv_m_gdo_20240101_20241221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'French Southern Territories: Copernicus Vegetation Index Anomaly (FAPAR
    Anomaly) (Data from 2023-01-01 to 2023-12-31)'
  download_url: https://data.humdata.org/dataset/f4695392-1536-4e15-9616-3bc04dc2f45c/resource/b085ee17-693e-4db7-9d5c-1f0b1aa6243f/download/atf_fpanv_m_gdo_20230101_20231221_t.zip
  format: null
  id: resource_b085ee17
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: atf_fpanv_m_gdo_20230101_20231221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'French Southern Territories: Copernicus Vegetation Index Anomaly (FAPAR
    Anomaly) (Data from 2022-01-01 to 2022-12-31)'
  download_url: https://data.humdata.org/dataset/f4695392-1536-4e15-9616-3bc04dc2f45c/resource/cb060dc5-1c22-46c6-b778-1c33b4229e99/download/atf_fpanv_m_gdo_20220101_20221221_t.zip
  format: null
  id: resource_cb060dc5
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: atf_fpanv_m_gdo_20220101_20221221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'French Southern Territories: Copernicus Vegetation Index Anomaly (FAPAR
    Anomaly) (Data from 2021-01-01 to 2021-12-31)'
  download_url: https://data.humdata.org/dataset/f4695392-1536-4e15-9616-3bc04dc2f45c/resource/6cb64d66-1896-49ce-996b-bb650a2bf2c4/download/atf_fpanv_m_gdo_20210101_20211221_t.zip
  format: null
  id: resource_6cb64d66
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: atf_fpanv_m_gdo_20210101_20211221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'French Southern Territories: Copernicus Vegetation Index Anomaly (FAPAR
    Anomaly) (Data from 2020-01-01 to 2020-12-31)'
  download_url: https://data.humdata.org/dataset/f4695392-1536-4e15-9616-3bc04dc2f45c/resource/3ce597c1-a880-4eef-b12d-01c517f88d4c/download/atf_fpanv_m_gdo_20200101_20201221_t.zip
  format: null
  id: resource_3ce597c1
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: atf_fpanv_m_gdo_20200101_20201221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'French Southern Territories: Copernicus Vegetation Index Anomaly (FAPAR
    Anomaly) (Data from 2019-01-01 to 2019-12-31)'
  download_url: https://data.humdata.org/dataset/f4695392-1536-4e15-9616-3bc04dc2f45c/resource/3270c9c7-5d1b-44a8-8902-e5109290d45d/download/atf_fpanv_m_gdo_20190101_20191221_t.zip
  format: null
  id: resource_3270c9c7
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: atf_fpanv_m_gdo_20190101_20191221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'French Southern Territories: Copernicus Vegetation Index Anomaly (FAPAR
    Anomaly) (Data from 2018-01-01 to 2018-12-31)'
  download_url: https://data.humdata.org/dataset/f4695392-1536-4e15-9616-3bc04dc2f45c/resource/0f3417c0-f072-494a-b954-581991bb94ed/download/atf_fpanv_m_gdo_20180101_20181221_t.zip
  format: null
  id: resource_0f3417c0
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: atf_fpanv_m_gdo_20180101_20181221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'French Southern Territories: Copernicus Vegetation Index Anomaly (FAPAR
    Anomaly) (Data from 2017-01-01 to 2017-12-31)'
  download_url: https://data.humdata.org/dataset/f4695392-1536-4e15-9616-3bc04dc2f45c/resource/850d4c48-1313-414f-893a-2eef2ca5c281/download/atf_fpanv_m_gdo_20170101_20171221_t.zip
  format: null
  id: resource_850d4c48
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: atf_fpanv_m_gdo_20170101_20171221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'French Southern Territories: Copernicus Vegetation Index Anomaly (FAPAR
    Anomaly) (Data from 2016-01-01 to 2016-12-31)'
  download_url: https://data.humdata.org/dataset/f4695392-1536-4e15-9616-3bc04dc2f45c/resource/8236eb37-4f88-4c24-9a7d-d8393dbd5c7f/download/atf_fpanv_m_gdo_20160101_20161221_t.zip
  format: null
  id: resource_8236eb37
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: atf_fpanv_m_gdo_20160101_20161221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'French Southern Territories: Copernicus Vegetation Index Anomaly (FAPAR
    Anomaly) (Data from 2015-01-01 to 2015-12-31)'
  download_url: https://data.humdata.org/dataset/f4695392-1536-4e15-9616-3bc04dc2f45c/resource/67cabdf5-bcba-4537-9b4d-5ba36e96115d/download/atf_fpanv_m_gdo_20150101_20151221_t.zip
  format: null
  id: resource_67cabdf5
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: atf_fpanv_m_gdo_20150101_20151221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'French Southern Territories: Copernicus Vegetation Index Anomaly (FAPAR
    Anomaly) (Data from 2014-01-01 to 2014-12-31)'
  download_url: https://data.humdata.org/dataset/f4695392-1536-4e15-9616-3bc04dc2f45c/resource/d230c5b9-22ec-4bfc-983a-b835e3a2051a/download/atf_fpanv_m_gdo_20140101_20141221_t.zip
  format: null
  id: resource_d230c5b9
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: atf_fpanv_m_gdo_20140101_20141221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'French Southern Territories: Copernicus Vegetation Index Anomaly (FAPAR
    Anomaly) (Data from 2013-01-01 to 2013-12-31)'
  download_url: https://data.humdata.org/dataset/f4695392-1536-4e15-9616-3bc04dc2f45c/resource/bce63c8e-971f-40b8-8294-bdfea06c0c90/download/atf_fpanv_m_gdo_20130101_20131221_t.zip
  format: null
  id: resource_bce63c8e
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: atf_fpanv_m_gdo_20130101_20131221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'French Southern Territories: Copernicus Vegetation Index Anomaly (FAPAR
    Anomaly) (Data from 2012-01-21 to 2012-12-31)'
  download_url: https://data.humdata.org/dataset/f4695392-1536-4e15-9616-3bc04dc2f45c/resource/beaaa051-5ae2-456e-810c-c57ec1092920/download/atf_fpanv_m_gdo_20120121_20121221_t.zip
  format: null
  id: resource_beaaa051
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: atf_fpanv_m_gdo_20120121_20121221_t.zip
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-atf_copernicus_frenchsouthernterritories_2012
spatial:
  bbox: null
  centroid: null
  countries:
  - ATF
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2026-01-10'
  start: '2012-01-21'
temporal_resolution: null
title: 'French Southern Territories: Copernicus Vegetation Index Anomaly (FAPAR Anomaly)'
version: null
vulnerability: null
---
