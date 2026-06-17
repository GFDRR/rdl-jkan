---
attributions:
- entity:
    affiliation: null
    email: null
    name: European Commission, Joint Research Centre (JRC)
    url: https://data.humdata.org/dataset/hkg-anomalies-fapar-viirs
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Copernicus
  url: https://data.humdata.org/dataset/hkg-anomalies-fapar-viirs
creator:
  affiliation: null
  email: null
  name: Copernicus
  url: https://data.humdata.org/dataset/hkg-anomalies-fapar-viirs
dataset_id: rdls_hzd-hkg_copernicus_chinahongkongspecialadmin_2012
description: 'Fraction of Absorbed Photosynthetically Active Radiation (FAPAR) is
  a biophysical dimensionless quantity (its values range from 0/no absorption to 1/total
  absorption) used to assess the greenness and health of vegetation. FAPAR anomalies
  can be used as an indicator to detect and monitor the impacts of agricultural drought
  on the growth and productivity of vegetation. The data is presented in 10-day time
  composite of the Visible Infrared Imaging Radiometer Suite (VIIRS).. [Source: This
  metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/hkg-anomalies-fapar-viirs]'
details: Variations in the vegetation health and/or cover could be related to stress
  factors not related to droughts (e.g., plant diseases, pests, hail, flooding). To
  determine if changes in FAPAR are linked with a drought event or not, FAPAR data
  should be interpreted jointly with other indicators (as in the EDO Combined Drought
  Indicator).
exposure: []
hazard:
  event_sets:
  - analysis_type: empirical
    calculation_method: inferred
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
  description: FAPAR values derived from VIIRS satellite radiometer data are processed
    into 10-day time composites. Anomalies are calculated at each grid cell as the
    deviation of FAPAR from a long-term mean baseline spanning 2012 to the most recent
    complete year, enabling detection and monitoring of agricultural drought impacts
    on vegetation productivity across Hong Kong.
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
- href: https://data.humdata.org/dataset/hkg-anomalies-fapar-viirs
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
  description: 'China, Hong Kong Special Administrative Region: Copernicus Vegetation
    Index Anomaly (FAPAR Anomaly) (Data from 2026-01-01 to 2026-01-10)'
  download_url: https://data.humdata.org/dataset/b73dbf30-f1df-4291-b976-907f032ed343/resource/fe077728-082c-4030-a089-017a3fd81daf/download/hkg_fpanv_m_gdo_20260101_20260101_t.zip
  format: null
  id: resource_fe077728
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hkg_fpanv_m_gdo_20260101_20260101_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'China, Hong Kong Special Administrative Region: Copernicus Vegetation
    Index Anomaly (FAPAR Anomaly) (Data from 2025-01-01 to 2025-12-31)'
  download_url: https://data.humdata.org/dataset/b73dbf30-f1df-4291-b976-907f032ed343/resource/c28d278b-1c18-4e26-884c-f69c038e504f/download/hkg_fpanv_m_gdo_20250101_20251221_t.zip
  format: null
  id: resource_c28d278b
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hkg_fpanv_m_gdo_20250101_20251221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'China, Hong Kong Special Administrative Region: Copernicus Vegetation
    Index Anomaly (FAPAR Anomaly) (Data from 2024-01-01 to 2024-12-31)'
  download_url: https://data.humdata.org/dataset/b73dbf30-f1df-4291-b976-907f032ed343/resource/781773ee-8ed6-47cb-83ce-abbc08ee9b64/download/hkg_fpanv_m_gdo_20240101_20241221_t.zip
  format: null
  id: resource_781773ee
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hkg_fpanv_m_gdo_20240101_20241221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'China, Hong Kong Special Administrative Region: Copernicus Vegetation
    Index Anomaly (FAPAR Anomaly) (Data from 2023-01-01 to 2023-12-31)'
  download_url: https://data.humdata.org/dataset/b73dbf30-f1df-4291-b976-907f032ed343/resource/d64b4baf-b43d-4958-a307-4630d7b6522a/download/hkg_fpanv_m_gdo_20230101_20231221_t.zip
  format: null
  id: resource_d64b4baf
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hkg_fpanv_m_gdo_20230101_20231221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'China, Hong Kong Special Administrative Region: Copernicus Vegetation
    Index Anomaly (FAPAR Anomaly) (Data from 2022-01-01 to 2022-12-31)'
  download_url: https://data.humdata.org/dataset/b73dbf30-f1df-4291-b976-907f032ed343/resource/451f2ebc-839c-4779-bad2-a72733674915/download/hkg_fpanv_m_gdo_20220101_20221221_t.zip
  format: null
  id: resource_451f2ebc
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hkg_fpanv_m_gdo_20220101_20221221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'China, Hong Kong Special Administrative Region: Copernicus Vegetation
    Index Anomaly (FAPAR Anomaly) (Data from 2021-01-01 to 2021-12-31)'
  download_url: https://data.humdata.org/dataset/b73dbf30-f1df-4291-b976-907f032ed343/resource/de5c1135-530d-4b9b-a3e6-de2a547ba047/download/hkg_fpanv_m_gdo_20210101_20211221_t.zip
  format: null
  id: resource_de5c1135
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hkg_fpanv_m_gdo_20210101_20211221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'China, Hong Kong Special Administrative Region: Copernicus Vegetation
    Index Anomaly (FAPAR Anomaly) (Data from 2020-01-01 to 2020-12-31)'
  download_url: https://data.humdata.org/dataset/b73dbf30-f1df-4291-b976-907f032ed343/resource/801c4088-7014-4e88-8b94-4e253ed75e2e/download/hkg_fpanv_m_gdo_20200101_20201221_t.zip
  format: null
  id: resource_801c4088
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hkg_fpanv_m_gdo_20200101_20201221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'China, Hong Kong Special Administrative Region: Copernicus Vegetation
    Index Anomaly (FAPAR Anomaly) (Data from 2019-01-01 to 2019-12-31)'
  download_url: https://data.humdata.org/dataset/b73dbf30-f1df-4291-b976-907f032ed343/resource/1f027d7b-3d97-43bf-ba3c-672b3f4af6cb/download/hkg_fpanv_m_gdo_20190101_20191221_t.zip
  format: null
  id: resource_1f027d7b
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hkg_fpanv_m_gdo_20190101_20191221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'China, Hong Kong Special Administrative Region: Copernicus Vegetation
    Index Anomaly (FAPAR Anomaly) (Data from 2018-01-01 to 2018-12-31)'
  download_url: https://data.humdata.org/dataset/b73dbf30-f1df-4291-b976-907f032ed343/resource/ad055e95-0a15-43c3-838e-c58148d80d21/download/hkg_fpanv_m_gdo_20180101_20181221_t.zip
  format: null
  id: resource_ad055e95
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hkg_fpanv_m_gdo_20180101_20181221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'China, Hong Kong Special Administrative Region: Copernicus Vegetation
    Index Anomaly (FAPAR Anomaly) (Data from 2017-01-01 to 2017-12-31)'
  download_url: https://data.humdata.org/dataset/b73dbf30-f1df-4291-b976-907f032ed343/resource/a401e45c-a449-40c7-b35a-3421c2a1046a/download/hkg_fpanv_m_gdo_20170101_20171221_t.zip
  format: null
  id: resource_a401e45c
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hkg_fpanv_m_gdo_20170101_20171221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'China, Hong Kong Special Administrative Region: Copernicus Vegetation
    Index Anomaly (FAPAR Anomaly) (Data from 2016-01-01 to 2016-12-31)'
  download_url: https://data.humdata.org/dataset/b73dbf30-f1df-4291-b976-907f032ed343/resource/316b1ae6-5b94-4e3d-8c66-04ea6ac3b146/download/hkg_fpanv_m_gdo_20160101_20161221_t.zip
  format: null
  id: resource_316b1ae6
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hkg_fpanv_m_gdo_20160101_20161221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'China, Hong Kong Special Administrative Region: Copernicus Vegetation
    Index Anomaly (FAPAR Anomaly) (Data from 2015-01-01 to 2015-12-31)'
  download_url: https://data.humdata.org/dataset/b73dbf30-f1df-4291-b976-907f032ed343/resource/44326a05-4086-4684-ac5a-446954a181e9/download/hkg_fpanv_m_gdo_20150101_20151221_t.zip
  format: null
  id: resource_44326a05
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hkg_fpanv_m_gdo_20150101_20151221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'China, Hong Kong Special Administrative Region: Copernicus Vegetation
    Index Anomaly (FAPAR Anomaly) (Data from 2014-01-01 to 2014-12-31)'
  download_url: https://data.humdata.org/dataset/b73dbf30-f1df-4291-b976-907f032ed343/resource/49876670-e95b-4230-b522-09fb278ff41a/download/hkg_fpanv_m_gdo_20140101_20141221_t.zip
  format: null
  id: resource_49876670
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hkg_fpanv_m_gdo_20140101_20141221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'China, Hong Kong Special Administrative Region: Copernicus Vegetation
    Index Anomaly (FAPAR Anomaly) (Data from 2013-01-01 to 2013-12-31)'
  download_url: https://data.humdata.org/dataset/b73dbf30-f1df-4291-b976-907f032ed343/resource/428e8d58-0969-403a-acf1-b7fcb200996c/download/hkg_fpanv_m_gdo_20130101_20131221_t.zip
  format: null
  id: resource_428e8d58
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hkg_fpanv_m_gdo_20130101_20131221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'China, Hong Kong Special Administrative Region: Copernicus Vegetation
    Index Anomaly (FAPAR Anomaly) (Data from 2012-01-21 to 2012-12-31)'
  download_url: https://data.humdata.org/dataset/b73dbf30-f1df-4291-b976-907f032ed343/resource/1551943a-1dc6-48e0-a63c-7551aee19df8/download/hkg_fpanv_m_gdo_20120121_20121221_t.zip
  format: null
  id: resource_1551943a
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hkg_fpanv_m_gdo_20120121_20121221_t.zip
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-hkg_copernicus_chinahongkongspecialadmin_2012
spatial:
  bbox: null
  centroid: null
  countries:
  - HKG
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2026-01-10'
  start: '2012-01-21'
temporal_resolution: null
title: 'China, Hong Kong Special Administrative Region: Copernicus Vegetation Index
  Anomaly (FAPAR Anomaly)'
version: null
vulnerability: null
---
