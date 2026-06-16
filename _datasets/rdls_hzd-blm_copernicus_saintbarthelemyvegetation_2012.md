---
attributions:
- entity:
    affiliation: null
    email: null
    name: European Commission, Joint Research Centre (JRC)
    url: https://data.humdata.org/dataset/blm-anomalies-fapar-viirs
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Copernicus
  url: https://data.humdata.org/dataset/blm-anomalies-fapar-viirs
creator:
  affiliation: null
  email: null
  name: Copernicus
  url: https://data.humdata.org/dataset/blm-anomalies-fapar-viirs
dataset_id: rdls_hzd-blm_copernicus_saintbarthelemyvegetation_2012
description: 'Fraction of Absorbed Photosynthetically Active Radiation (FAPAR) is
  a biophysical dimensionless quantity (its values range from 0/no absorption to 1/total
  absorption) used to assess the greenness and health of vegetation. FAPAR anomalies
  can be used as an indicator to detect and monitor the impacts of agricultural drought
  on the growth and productivity of vegetation. The data is presented in 10-day time
  composite of the Visible Infrared Imaging Radiometer Suite (VIIRS).. [Source: This
  metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/blm-anomalies-fapar-viirs]'
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
  description: FAPAR values are derived from VIIRS satellite observations at 10-day
    intervals. Anomalies are calculated by computing the deviation of FAPAR from the
    long-term mean (2012 to last available full year) at each grid cell. The resulting
    raster datasets are provided as GeoTIFF files for annual periods from 2012 to
    2026, enabling temporal monitoring of vegetation stress as an indicator of agricultural
    drought impacts.
  sources:
  - id: source_1
    license: null
    name: European Commission, Joint Research Centre (JRC)
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
  - id: source_2
    license: null
    name: Copernicus
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/blm-anomalies-fapar-viirs
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
  description: "Saint Barth\xE9lemy: Copernicus Vegetation Index Anomaly (FAPAR Anomaly)\
    \ (Data from 2026-01-01 to 2026-01-10)"
  download_url: https://data.humdata.org/dataset/d30d3477-4d62-4b39-96e5-bd31cce01ddb/resource/2eda1336-d1b3-477f-950d-55154fd24145/download/blm_fpanv_m_gdo_20260101_20260101_t.zip
  format: null
  id: resource_2eda1336
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: blm_fpanv_m_gdo_20260101_20260101_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Saint Barth\xE9lemy: Copernicus Vegetation Index Anomaly (FAPAR Anomaly)\
    \ (Data from 2025-01-01 to 2025-12-31)"
  download_url: https://data.humdata.org/dataset/d30d3477-4d62-4b39-96e5-bd31cce01ddb/resource/4114fc66-5026-4e89-ad59-5a8ef80f0a2b/download/blm_fpanv_m_gdo_20250101_20251221_t.zip
  format: null
  id: resource_4114fc66
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: blm_fpanv_m_gdo_20250101_20251221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Saint Barth\xE9lemy: Copernicus Vegetation Index Anomaly (FAPAR Anomaly)\
    \ (Data from 2024-01-01 to 2024-12-31)"
  download_url: https://data.humdata.org/dataset/d30d3477-4d62-4b39-96e5-bd31cce01ddb/resource/f8599e66-80e9-4af6-ae62-e3346fcb89a2/download/blm_fpanv_m_gdo_20240101_20241221_t.zip
  format: null
  id: resource_f8599e66
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: blm_fpanv_m_gdo_20240101_20241221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Saint Barth\xE9lemy: Copernicus Vegetation Index Anomaly (FAPAR Anomaly)\
    \ (Data from 2023-01-01 to 2023-12-31)"
  download_url: https://data.humdata.org/dataset/d30d3477-4d62-4b39-96e5-bd31cce01ddb/resource/d329d507-202d-4d9c-86f9-67af9531425e/download/blm_fpanv_m_gdo_20230101_20231221_t.zip
  format: null
  id: resource_d329d507
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: blm_fpanv_m_gdo_20230101_20231221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Saint Barth\xE9lemy: Copernicus Vegetation Index Anomaly (FAPAR Anomaly)\
    \ (Data from 2022-01-01 to 2022-12-31)"
  download_url: https://data.humdata.org/dataset/d30d3477-4d62-4b39-96e5-bd31cce01ddb/resource/ed5316f6-f177-44f7-8df6-3a44d6bfd3da/download/blm_fpanv_m_gdo_20220101_20221221_t.zip
  format: null
  id: resource_ed5316f6
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: blm_fpanv_m_gdo_20220101_20221221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Saint Barth\xE9lemy: Copernicus Vegetation Index Anomaly (FAPAR Anomaly)\
    \ (Data from 2021-01-01 to 2021-12-31)"
  download_url: https://data.humdata.org/dataset/d30d3477-4d62-4b39-96e5-bd31cce01ddb/resource/47c442f6-91ce-4feb-a1bd-d08107549178/download/blm_fpanv_m_gdo_20210101_20211221_t.zip
  format: null
  id: resource_47c442f6
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: blm_fpanv_m_gdo_20210101_20211221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Saint Barth\xE9lemy: Copernicus Vegetation Index Anomaly (FAPAR Anomaly)\
    \ (Data from 2020-01-01 to 2020-12-31)"
  download_url: https://data.humdata.org/dataset/d30d3477-4d62-4b39-96e5-bd31cce01ddb/resource/121f6451-df5b-45ef-975b-e58e1e388d31/download/blm_fpanv_m_gdo_20200101_20201221_t.zip
  format: null
  id: resource_121f6451
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: blm_fpanv_m_gdo_20200101_20201221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Saint Barth\xE9lemy: Copernicus Vegetation Index Anomaly (FAPAR Anomaly)\
    \ (Data from 2019-01-01 to 2019-12-31)"
  download_url: https://data.humdata.org/dataset/d30d3477-4d62-4b39-96e5-bd31cce01ddb/resource/502c9d4a-01e5-4cf9-a933-fd3ad40fb4a1/download/blm_fpanv_m_gdo_20190101_20191221_t.zip
  format: null
  id: resource_502c9d4a
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: blm_fpanv_m_gdo_20190101_20191221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Saint Barth\xE9lemy: Copernicus Vegetation Index Anomaly (FAPAR Anomaly)\
    \ (Data from 2018-01-01 to 2018-12-31)"
  download_url: https://data.humdata.org/dataset/d30d3477-4d62-4b39-96e5-bd31cce01ddb/resource/aee6b063-0f65-48f1-b271-3b8659472835/download/blm_fpanv_m_gdo_20180101_20181221_t.zip
  format: null
  id: resource_aee6b063
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: blm_fpanv_m_gdo_20180101_20181221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Saint Barth\xE9lemy: Copernicus Vegetation Index Anomaly (FAPAR Anomaly)\
    \ (Data from 2017-01-01 to 2017-12-31)"
  download_url: https://data.humdata.org/dataset/d30d3477-4d62-4b39-96e5-bd31cce01ddb/resource/9c0850ee-9e94-4e91-82a5-40966d56e9a7/download/blm_fpanv_m_gdo_20170101_20171221_t.zip
  format: null
  id: resource_9c0850ee
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: blm_fpanv_m_gdo_20170101_20171221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Saint Barth\xE9lemy: Copernicus Vegetation Index Anomaly (FAPAR Anomaly)\
    \ (Data from 2016-01-01 to 2016-12-31)"
  download_url: https://data.humdata.org/dataset/d30d3477-4d62-4b39-96e5-bd31cce01ddb/resource/9d170a0a-c041-4a3a-b086-f3c7a6b7fe1a/download/blm_fpanv_m_gdo_20160101_20161221_t.zip
  format: null
  id: resource_9d170a0a
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: blm_fpanv_m_gdo_20160101_20161221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Saint Barth\xE9lemy: Copernicus Vegetation Index Anomaly (FAPAR Anomaly)\
    \ (Data from 2015-01-01 to 2015-12-31)"
  download_url: https://data.humdata.org/dataset/d30d3477-4d62-4b39-96e5-bd31cce01ddb/resource/8f82f57c-bcc5-43ba-a7ea-a3d5b41c14be/download/blm_fpanv_m_gdo_20150101_20151221_t.zip
  format: null
  id: resource_8f82f57c
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: blm_fpanv_m_gdo_20150101_20151221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Saint Barth\xE9lemy: Copernicus Vegetation Index Anomaly (FAPAR Anomaly)\
    \ (Data from 2014-01-01 to 2014-12-31)"
  download_url: https://data.humdata.org/dataset/d30d3477-4d62-4b39-96e5-bd31cce01ddb/resource/0396091d-804f-4a4b-bf3f-648cf189059c/download/blm_fpanv_m_gdo_20140101_20141221_t.zip
  format: null
  id: resource_0396091d
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: blm_fpanv_m_gdo_20140101_20141221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Saint Barth\xE9lemy: Copernicus Vegetation Index Anomaly (FAPAR Anomaly)\
    \ (Data from 2013-01-01 to 2013-12-31)"
  download_url: https://data.humdata.org/dataset/d30d3477-4d62-4b39-96e5-bd31cce01ddb/resource/356aa11f-f2b6-4660-ad7c-ff6a91fb76bb/download/blm_fpanv_m_gdo_20130101_20131221_t.zip
  format: null
  id: resource_356aa11f
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: blm_fpanv_m_gdo_20130101_20131221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Saint Barth\xE9lemy: Copernicus Vegetation Index Anomaly (FAPAR Anomaly)\
    \ (Data from 2012-01-21 to 2012-12-31)"
  download_url: https://data.humdata.org/dataset/d30d3477-4d62-4b39-96e5-bd31cce01ddb/resource/fb04f535-e730-44f1-b7a9-4c1eeb100fa4/download/blm_fpanv_m_gdo_20120121_20121221_t.zip
  format: null
  id: resource_fb04f535
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: blm_fpanv_m_gdo_20120121_20121221_t.zip
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-blm_copernicus_saintbarthelemyvegetation_2012
spatial:
  bbox: null
  centroid: null
  countries:
  - BLM
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2026-01-10'
  start: '2012-01-21'
temporal_resolution: null
title: "Saint Barth\xE9lemy: Copernicus Vegetation Index Anomaly (FAPAR Anomaly)"
version: null
vulnerability: null
---
