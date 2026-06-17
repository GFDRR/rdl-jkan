---
attributions:
- entity:
    affiliation: null
    email: null
    name: European Commission, Joint Research Centre (JRC)
    url: https://data.humdata.org/dataset/mhl-anomalies-fapar-viirs
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Copernicus
  url: https://data.humdata.org/dataset/mhl-anomalies-fapar-viirs
creator:
  affiliation: null
  email: null
  name: Copernicus
  url: https://data.humdata.org/dataset/mhl-anomalies-fapar-viirs
dataset_id: rdls_hzd-mhl_copernicus_marshallislandsvegetation_2012
description: 'Fraction of Absorbed Photosynthetically Active Radiation (FAPAR) is
  a biophysical dimensionless quantity (its values range from 0/no absorption to 1/total
  absorption) used to assess the greenness and health of vegetation. FAPAR anomalies
  can be used as an indicator to detect and monitor the impacts of agricultural drought
  on the growth and productivity of vegetation. The data is presented in 10-day time
  composite of the Visible Infrared Imaging Radiometer Suite (VIIRS).. [Source: This
  metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/mhl-anomalies-fapar-viirs]'
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
  description: FAPAR values from VIIRS satellite observations are processed into 10-day
    temporal composites. Anomalies are calculated at each grid cell by computing the
    deviation from a long-term mean baseline (2012 to the last available full year),
    enabling detection and monitoring of agricultural drought impacts on vegetation
    productivity across the Marshall Islands.
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
- href: https://data.humdata.org/dataset/mhl-anomalies-fapar-viirs
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
  description: 'Marshall Islands: Copernicus Vegetation Index Anomaly (FAPAR Anomaly)
    (Data from 2026-01-01 to 2026-01-10)'
  download_url: https://data.humdata.org/dataset/a0421ff2-c1b4-4451-a844-40995e370eeb/resource/47ba653d-d08a-432a-b8ec-40b7062032d1/download/mhl_fpanv_m_gdo_20260101_20260101_t.zip
  format: null
  id: resource_47ba653d
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mhl_fpanv_m_gdo_20260101_20260101_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Marshall Islands: Copernicus Vegetation Index Anomaly (FAPAR Anomaly)
    (Data from 2025-01-01 to 2025-12-31)'
  download_url: https://data.humdata.org/dataset/a0421ff2-c1b4-4451-a844-40995e370eeb/resource/4939d935-ec61-40f0-9d7c-12058d54b0c2/download/mhl_fpanv_m_gdo_20250101_20251221_t.zip
  format: null
  id: resource_4939d935
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mhl_fpanv_m_gdo_20250101_20251221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Marshall Islands: Copernicus Vegetation Index Anomaly (FAPAR Anomaly)
    (Data from 2024-01-01 to 2024-12-31)'
  download_url: https://data.humdata.org/dataset/a0421ff2-c1b4-4451-a844-40995e370eeb/resource/b6ad74aa-222b-448f-b211-ce628b98bfb3/download/mhl_fpanv_m_gdo_20240101_20241221_t.zip
  format: null
  id: resource_b6ad74aa
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mhl_fpanv_m_gdo_20240101_20241221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Marshall Islands: Copernicus Vegetation Index Anomaly (FAPAR Anomaly)
    (Data from 2023-01-01 to 2023-12-31)'
  download_url: https://data.humdata.org/dataset/a0421ff2-c1b4-4451-a844-40995e370eeb/resource/73e72d3f-e9d4-4568-b1cf-8a460c77d76c/download/mhl_fpanv_m_gdo_20230101_20231221_t.zip
  format: null
  id: resource_73e72d3f
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mhl_fpanv_m_gdo_20230101_20231221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Marshall Islands: Copernicus Vegetation Index Anomaly (FAPAR Anomaly)
    (Data from 2022-01-01 to 2022-12-31)'
  download_url: https://data.humdata.org/dataset/a0421ff2-c1b4-4451-a844-40995e370eeb/resource/67865f71-aa74-47fb-aac0-fd204e07596d/download/mhl_fpanv_m_gdo_20220101_20221221_t.zip
  format: null
  id: resource_67865f71
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mhl_fpanv_m_gdo_20220101_20221221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Marshall Islands: Copernicus Vegetation Index Anomaly (FAPAR Anomaly)
    (Data from 2021-01-01 to 2021-12-31)'
  download_url: https://data.humdata.org/dataset/a0421ff2-c1b4-4451-a844-40995e370eeb/resource/15c72553-b600-4000-9c66-0d64bbea9c60/download/mhl_fpanv_m_gdo_20210101_20211221_t.zip
  format: null
  id: resource_15c72553
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mhl_fpanv_m_gdo_20210101_20211221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Marshall Islands: Copernicus Vegetation Index Anomaly (FAPAR Anomaly)
    (Data from 2020-01-01 to 2020-12-31)'
  download_url: https://data.humdata.org/dataset/a0421ff2-c1b4-4451-a844-40995e370eeb/resource/6f338b61-dcd3-443e-b36e-dbcfa1585e95/download/mhl_fpanv_m_gdo_20200101_20201221_t.zip
  format: null
  id: resource_6f338b61
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mhl_fpanv_m_gdo_20200101_20201221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Marshall Islands: Copernicus Vegetation Index Anomaly (FAPAR Anomaly)
    (Data from 2019-01-01 to 2019-12-31)'
  download_url: https://data.humdata.org/dataset/a0421ff2-c1b4-4451-a844-40995e370eeb/resource/f45ee6b1-cdac-4902-bfdd-14aec9262245/download/mhl_fpanv_m_gdo_20190101_20191221_t.zip
  format: null
  id: resource_f45ee6b1
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mhl_fpanv_m_gdo_20190101_20191221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Marshall Islands: Copernicus Vegetation Index Anomaly (FAPAR Anomaly)
    (Data from 2018-01-01 to 2018-12-31)'
  download_url: https://data.humdata.org/dataset/a0421ff2-c1b4-4451-a844-40995e370eeb/resource/993a7b21-809d-43d2-b8ed-4fd4da55b8bc/download/mhl_fpanv_m_gdo_20180101_20181221_t.zip
  format: null
  id: resource_993a7b21
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mhl_fpanv_m_gdo_20180101_20181221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Marshall Islands: Copernicus Vegetation Index Anomaly (FAPAR Anomaly)
    (Data from 2017-01-01 to 2017-12-31)'
  download_url: https://data.humdata.org/dataset/a0421ff2-c1b4-4451-a844-40995e370eeb/resource/77eb145a-e969-496f-924e-4bb8ead2b43f/download/mhl_fpanv_m_gdo_20170101_20171221_t.zip
  format: null
  id: resource_77eb145a
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mhl_fpanv_m_gdo_20170101_20171221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Marshall Islands: Copernicus Vegetation Index Anomaly (FAPAR Anomaly)
    (Data from 2016-01-01 to 2016-12-31)'
  download_url: https://data.humdata.org/dataset/a0421ff2-c1b4-4451-a844-40995e370eeb/resource/ace25df7-15b4-48e5-b5c3-21e62784766f/download/mhl_fpanv_m_gdo_20160101_20161221_t.zip
  format: null
  id: resource_ace25df7
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mhl_fpanv_m_gdo_20160101_20161221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Marshall Islands: Copernicus Vegetation Index Anomaly (FAPAR Anomaly)
    (Data from 2015-01-01 to 2015-12-31)'
  download_url: https://data.humdata.org/dataset/a0421ff2-c1b4-4451-a844-40995e370eeb/resource/b7834718-dd79-4d59-a6ea-fa7c36ca3955/download/mhl_fpanv_m_gdo_20150101_20151221_t.zip
  format: null
  id: resource_b7834718
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mhl_fpanv_m_gdo_20150101_20151221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Marshall Islands: Copernicus Vegetation Index Anomaly (FAPAR Anomaly)
    (Data from 2014-01-01 to 2014-12-31)'
  download_url: https://data.humdata.org/dataset/a0421ff2-c1b4-4451-a844-40995e370eeb/resource/8982a886-01fb-43f2-a96b-dbe004f47f83/download/mhl_fpanv_m_gdo_20140101_20141221_t.zip
  format: null
  id: resource_8982a886
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mhl_fpanv_m_gdo_20140101_20141221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Marshall Islands: Copernicus Vegetation Index Anomaly (FAPAR Anomaly)
    (Data from 2013-01-01 to 2013-12-31)'
  download_url: https://data.humdata.org/dataset/a0421ff2-c1b4-4451-a844-40995e370eeb/resource/f73416f7-447c-43c6-b2d0-f7cf188eb54c/download/mhl_fpanv_m_gdo_20130101_20131221_t.zip
  format: null
  id: resource_f73416f7
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mhl_fpanv_m_gdo_20130101_20131221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Marshall Islands: Copernicus Vegetation Index Anomaly (FAPAR Anomaly)
    (Data from 2012-01-21 to 2012-12-31)'
  download_url: https://data.humdata.org/dataset/a0421ff2-c1b4-4451-a844-40995e370eeb/resource/4e8e2a77-f559-41af-9736-e88a02d4c927/download/mhl_fpanv_m_gdo_20120121_20121221_t.zip
  format: null
  id: resource_4e8e2a77
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mhl_fpanv_m_gdo_20120121_20121221_t.zip
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-mhl_copernicus_marshallislandsvegetation_2012
spatial:
  bbox: null
  centroid: null
  countries:
  - MHL
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2026-01-10'
  start: '2012-01-21'
temporal_resolution: null
title: 'Marshall Islands: Copernicus Vegetation Index Anomaly (FAPAR Anomaly)'
version: null
vulnerability: null
---
