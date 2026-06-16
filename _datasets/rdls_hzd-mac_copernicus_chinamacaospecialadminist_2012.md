---
attributions:
- entity:
    affiliation: null
    email: null
    name: Copernicus Vegetation Index (VIIRS)
    url: https://data.humdata.org/dataset/mac-anomalies-fapar-viirs
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Copernicus
  url: https://data.humdata.org/dataset/mac-anomalies-fapar-viirs
creator:
  affiliation: null
  email: null
  name: Copernicus
  url: https://data.humdata.org/dataset/mac-anomalies-fapar-viirs
dataset_id: rdls_hzd-mac_copernicus_chinamacaospecialadminist_2012
description: 'Fraction of Absorbed Photosynthetically Active Radiation (FAPAR) is
  a biophysical dimensionless quantity (its values range from 0/no absorption to 1/total
  absorption) used to assess the greenness and health of vegetation. FAPAR anomalies
  can be used as an indicator to detect and monitor the impacts of agricultural drought
  on the growth and productivity of vegetation. The data is presented in 10-day time
  composite of the Visible Infrared Imaging Radiometer Suite (VIIRS).. [Source: This
  metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/mac-anomalies-fapar-viirs]'
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
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: FAPAR values from VIIRS satellite observations are composited at 10-day
    intervals and processed into anomalies by calculating the deviation from long-term
    mean values (baseline 2012 to last available full year) at each grid cell to create
    raster datasets for drought monitoring and vegetation health assessment.
  sources:
  - id: source_1
    license: null
    name: Copernicus Vegetation Index (VIIRS)
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/mac-anomalies-fapar-viirs
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
  description: 'China, Macao Special Administrative Region: Copernicus Vegetation
    Index Anomaly (FAPAR Anomaly) (Data from 2026-01-01 to 2026-01-10)'
  download_url: https://data.humdata.org/dataset/6959935c-131f-4dc0-9e46-4e98eb54d3c1/resource/04df68b6-7558-47f4-83fa-47da7ed07f2d/download/mac_fpanv_m_gdo_20260101_20260101_t.zip
  format: null
  id: resource_04df68b6
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mac_fpanv_m_gdo_20260101_20260101_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'China, Macao Special Administrative Region: Copernicus Vegetation
    Index Anomaly (FAPAR Anomaly) (Data from 2025-01-01 to 2025-12-31)'
  download_url: https://data.humdata.org/dataset/6959935c-131f-4dc0-9e46-4e98eb54d3c1/resource/c434c240-d1c1-4451-ad79-c6961c88b60d/download/mac_fpanv_m_gdo_20250101_20251221_t.zip
  format: null
  id: resource_c434c240
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mac_fpanv_m_gdo_20250101_20251221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'China, Macao Special Administrative Region: Copernicus Vegetation
    Index Anomaly (FAPAR Anomaly) (Data from 2024-01-01 to 2024-12-31)'
  download_url: https://data.humdata.org/dataset/6959935c-131f-4dc0-9e46-4e98eb54d3c1/resource/f0616eae-1ea4-4f3f-8f6d-b78f434b2c68/download/mac_fpanv_m_gdo_20240101_20241221_t.zip
  format: null
  id: resource_f0616eae
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mac_fpanv_m_gdo_20240101_20241221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'China, Macao Special Administrative Region: Copernicus Vegetation
    Index Anomaly (FAPAR Anomaly) (Data from 2023-01-01 to 2023-12-31)'
  download_url: https://data.humdata.org/dataset/6959935c-131f-4dc0-9e46-4e98eb54d3c1/resource/4bb40189-808f-4111-a5df-ca2a5a952b60/download/mac_fpanv_m_gdo_20230101_20231221_t.zip
  format: null
  id: resource_4bb40189
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mac_fpanv_m_gdo_20230101_20231221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'China, Macao Special Administrative Region: Copernicus Vegetation
    Index Anomaly (FAPAR Anomaly) (Data from 2022-01-01 to 2022-12-31)'
  download_url: https://data.humdata.org/dataset/6959935c-131f-4dc0-9e46-4e98eb54d3c1/resource/abe57fa3-e11a-44a6-8c57-2c9af6b538d3/download/mac_fpanv_m_gdo_20220101_20221221_t.zip
  format: null
  id: resource_abe57fa3
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mac_fpanv_m_gdo_20220101_20221221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'China, Macao Special Administrative Region: Copernicus Vegetation
    Index Anomaly (FAPAR Anomaly) (Data from 2021-01-01 to 2021-12-31)'
  download_url: https://data.humdata.org/dataset/6959935c-131f-4dc0-9e46-4e98eb54d3c1/resource/3a82164b-f7bb-49b8-87e6-b6b8a2a9d0be/download/mac_fpanv_m_gdo_20210101_20211221_t.zip
  format: null
  id: resource_3a82164b
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mac_fpanv_m_gdo_20210101_20211221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'China, Macao Special Administrative Region: Copernicus Vegetation
    Index Anomaly (FAPAR Anomaly) (Data from 2020-01-01 to 2020-12-31)'
  download_url: https://data.humdata.org/dataset/6959935c-131f-4dc0-9e46-4e98eb54d3c1/resource/cd05f7c7-0d03-4542-8515-2c3e2738352b/download/mac_fpanv_m_gdo_20200101_20201221_t.zip
  format: null
  id: resource_cd05f7c7
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mac_fpanv_m_gdo_20200101_20201221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'China, Macao Special Administrative Region: Copernicus Vegetation
    Index Anomaly (FAPAR Anomaly) (Data from 2019-01-01 to 2019-12-31)'
  download_url: https://data.humdata.org/dataset/6959935c-131f-4dc0-9e46-4e98eb54d3c1/resource/bcc5be6b-abe8-4680-9917-edd8895e9656/download/mac_fpanv_m_gdo_20190101_20191221_t.zip
  format: null
  id: resource_bcc5be6b
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mac_fpanv_m_gdo_20190101_20191221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'China, Macao Special Administrative Region: Copernicus Vegetation
    Index Anomaly (FAPAR Anomaly) (Data from 2018-01-01 to 2018-12-31)'
  download_url: https://data.humdata.org/dataset/6959935c-131f-4dc0-9e46-4e98eb54d3c1/resource/20c4832b-7dd9-4f2e-b615-a30d8ce4a30f/download/mac_fpanv_m_gdo_20180101_20181221_t.zip
  format: null
  id: resource_20c4832b
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mac_fpanv_m_gdo_20180101_20181221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'China, Macao Special Administrative Region: Copernicus Vegetation
    Index Anomaly (FAPAR Anomaly) (Data from 2017-01-01 to 2017-12-31)'
  download_url: https://data.humdata.org/dataset/6959935c-131f-4dc0-9e46-4e98eb54d3c1/resource/3daa0892-d2e8-4542-9b6c-22b03f9be64f/download/mac_fpanv_m_gdo_20170101_20171221_t.zip
  format: null
  id: resource_3daa0892
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mac_fpanv_m_gdo_20170101_20171221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'China, Macao Special Administrative Region: Copernicus Vegetation
    Index Anomaly (FAPAR Anomaly) (Data from 2016-01-01 to 2016-12-31)'
  download_url: https://data.humdata.org/dataset/6959935c-131f-4dc0-9e46-4e98eb54d3c1/resource/d7a6be5d-99bf-43b1-b176-e3cefb590cb5/download/mac_fpanv_m_gdo_20160101_20161221_t.zip
  format: null
  id: resource_d7a6be5d
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mac_fpanv_m_gdo_20160101_20161221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'China, Macao Special Administrative Region: Copernicus Vegetation
    Index Anomaly (FAPAR Anomaly) (Data from 2015-01-01 to 2015-12-31)'
  download_url: https://data.humdata.org/dataset/6959935c-131f-4dc0-9e46-4e98eb54d3c1/resource/3cd43098-86de-476c-8a5d-e66909fa8f62/download/mac_fpanv_m_gdo_20150101_20151221_t.zip
  format: null
  id: resource_3cd43098
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mac_fpanv_m_gdo_20150101_20151221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'China, Macao Special Administrative Region: Copernicus Vegetation
    Index Anomaly (FAPAR Anomaly) (Data from 2014-01-01 to 2014-12-31)'
  download_url: https://data.humdata.org/dataset/6959935c-131f-4dc0-9e46-4e98eb54d3c1/resource/79f33b43-7163-4396-962d-4dcb46f85200/download/mac_fpanv_m_gdo_20140101_20141221_t.zip
  format: null
  id: resource_79f33b43
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mac_fpanv_m_gdo_20140101_20141221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'China, Macao Special Administrative Region: Copernicus Vegetation
    Index Anomaly (FAPAR Anomaly) (Data from 2013-01-01 to 2013-12-31)'
  download_url: https://data.humdata.org/dataset/6959935c-131f-4dc0-9e46-4e98eb54d3c1/resource/f60683cf-5f4f-4c27-9d01-f8f50c397ac1/download/mac_fpanv_m_gdo_20130101_20131221_t.zip
  format: null
  id: resource_f60683cf
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mac_fpanv_m_gdo_20130101_20131221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'China, Macao Special Administrative Region: Copernicus Vegetation
    Index Anomaly (FAPAR Anomaly) (Data from 2012-01-21 to 2012-12-31)'
  download_url: https://data.humdata.org/dataset/6959935c-131f-4dc0-9e46-4e98eb54d3c1/resource/185ec444-0d5b-497b-88ca-d66fa9f3e758/download/mac_fpanv_m_gdo_20120121_20121221_t.zip
  format: null
  id: resource_185ec444
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mac_fpanv_m_gdo_20120121_20121221_t.zip
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-mac_copernicus_chinamacaospecialadminist_2012
spatial:
  bbox: null
  centroid: null
  countries:
  - MAC
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2026-01-10'
  start: '2012-01-21'
temporal_resolution: null
title: 'China, Macao Special Administrative Region: Copernicus Vegetation Index Anomaly
  (FAPAR Anomaly)'
version: null
vulnerability: null
---
