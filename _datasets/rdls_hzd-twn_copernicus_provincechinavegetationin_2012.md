---
attributions:
- entity:
    affiliation: null
    email: null
    name: European Commission, Joint Research Centre (JRC)
    url: https://data.humdata.org/dataset/twn-anomalies-fapar-viirs
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Copernicus
  url: https://data.humdata.org/dataset/twn-anomalies-fapar-viirs
creator:
  affiliation: null
  email: null
  name: Copernicus
  url: https://data.humdata.org/dataset/twn-anomalies-fapar-viirs
dataset_id: rdls_hzd-twn_copernicus_provincechinavegetationin_2012
description: 'Fraction of Absorbed Photosynthetically Active Radiation (FAPAR) is
  a biophysical dimensionless quantity (its values range from 0/no absorption to 1/total
  absorption) used to assess the greenness and health of vegetation. FAPAR anomalies
  can be used as an indicator to detect and monitor the impacts of agricultural drought
  on the growth and productivity of vegetation. The data is presented in 10-day time
  composite of the Visible Infrared Imaging Radiometer Suite (VIIRS).. [Source: This
  metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/twn-anomalies-fapar-viirs]'
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
  description: FAPAR values are derived from VIIRS satellite observations at 10-day
    intervals. Anomalies are calculated by computing the deviation of each grid cell's
    FAPAR value from its long-term mean baseline (2012 to the last complete year),
    producing dimensionless raster datasets that quantify vegetation stress relative
    to historical norms for agricultural drought monitoring.
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
- href: https://data.humdata.org/dataset/twn-anomalies-fapar-viirs
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
  description: 'Taiwan (Province of China): Copernicus Vegetation Index Anomaly (FAPAR
    Anomaly) (Data from 2026-01-01 to 2026-01-10)'
  download_url: https://data.humdata.org/dataset/e10e47e9-b757-4a10-8940-5ee752d4442b/resource/4ae87536-7928-46a6-b3f9-ec1dfe5699cd/download/twn_fpanv_m_gdo_20260101_20260101_t.zip
  format: null
  id: resource_4ae87536
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: twn_fpanv_m_gdo_20260101_20260101_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Taiwan (Province of China): Copernicus Vegetation Index Anomaly (FAPAR
    Anomaly) (Data from 2025-01-01 to 2025-12-31)'
  download_url: https://data.humdata.org/dataset/e10e47e9-b757-4a10-8940-5ee752d4442b/resource/07fa1694-9154-4dd9-8623-c28996567681/download/twn_fpanv_m_gdo_20250101_20251221_t.zip
  format: null
  id: resource_07fa1694
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: twn_fpanv_m_gdo_20250101_20251221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Taiwan (Province of China): Copernicus Vegetation Index Anomaly (FAPAR
    Anomaly) (Data from 2024-01-01 to 2024-12-31)'
  download_url: https://data.humdata.org/dataset/e10e47e9-b757-4a10-8940-5ee752d4442b/resource/6203bb14-abce-4890-99bf-b65c8bdd6cfb/download/twn_fpanv_m_gdo_20240101_20241221_t.zip
  format: null
  id: resource_6203bb14
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: twn_fpanv_m_gdo_20240101_20241221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Taiwan (Province of China): Copernicus Vegetation Index Anomaly (FAPAR
    Anomaly) (Data from 2023-01-01 to 2023-12-31)'
  download_url: https://data.humdata.org/dataset/e10e47e9-b757-4a10-8940-5ee752d4442b/resource/3a59824a-324e-4687-bd12-030082f378be/download/twn_fpanv_m_gdo_20230101_20231221_t.zip
  format: null
  id: resource_3a59824a
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: twn_fpanv_m_gdo_20230101_20231221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Taiwan (Province of China): Copernicus Vegetation Index Anomaly (FAPAR
    Anomaly) (Data from 2022-01-01 to 2022-12-31)'
  download_url: https://data.humdata.org/dataset/e10e47e9-b757-4a10-8940-5ee752d4442b/resource/b1786f85-58c9-4863-85af-420570b24888/download/twn_fpanv_m_gdo_20220101_20221221_t.zip
  format: null
  id: resource_b1786f85
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: twn_fpanv_m_gdo_20220101_20221221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Taiwan (Province of China): Copernicus Vegetation Index Anomaly (FAPAR
    Anomaly) (Data from 2021-01-01 to 2021-12-31)'
  download_url: https://data.humdata.org/dataset/e10e47e9-b757-4a10-8940-5ee752d4442b/resource/fb737f54-1f25-4d0f-9b58-779e0ed72590/download/twn_fpanv_m_gdo_20210101_20211221_t.zip
  format: null
  id: resource_fb737f54
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: twn_fpanv_m_gdo_20210101_20211221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Taiwan (Province of China): Copernicus Vegetation Index Anomaly (FAPAR
    Anomaly) (Data from 2020-01-01 to 2020-12-31)'
  download_url: https://data.humdata.org/dataset/e10e47e9-b757-4a10-8940-5ee752d4442b/resource/feb0bf30-c820-4287-913c-3db3a6a17afd/download/twn_fpanv_m_gdo_20200101_20201221_t.zip
  format: null
  id: resource_feb0bf30
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: twn_fpanv_m_gdo_20200101_20201221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Taiwan (Province of China): Copernicus Vegetation Index Anomaly (FAPAR
    Anomaly) (Data from 2019-01-01 to 2019-12-31)'
  download_url: https://data.humdata.org/dataset/e10e47e9-b757-4a10-8940-5ee752d4442b/resource/0a81635e-1a26-4fab-9ff9-56198b0c8ff7/download/twn_fpanv_m_gdo_20190101_20191221_t.zip
  format: null
  id: resource_0a81635e
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: twn_fpanv_m_gdo_20190101_20191221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Taiwan (Province of China): Copernicus Vegetation Index Anomaly (FAPAR
    Anomaly) (Data from 2018-01-01 to 2018-12-31)'
  download_url: https://data.humdata.org/dataset/e10e47e9-b757-4a10-8940-5ee752d4442b/resource/ce7c8798-f9df-44bc-849b-593d63912873/download/twn_fpanv_m_gdo_20180101_20181221_t.zip
  format: null
  id: resource_ce7c8798
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: twn_fpanv_m_gdo_20180101_20181221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Taiwan (Province of China): Copernicus Vegetation Index Anomaly (FAPAR
    Anomaly) (Data from 2017-01-01 to 2017-12-31)'
  download_url: https://data.humdata.org/dataset/e10e47e9-b757-4a10-8940-5ee752d4442b/resource/8120bc1f-9fe0-43df-bf68-b4789fca6ca3/download/twn_fpanv_m_gdo_20170101_20171221_t.zip
  format: null
  id: resource_8120bc1f
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: twn_fpanv_m_gdo_20170101_20171221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Taiwan (Province of China): Copernicus Vegetation Index Anomaly (FAPAR
    Anomaly) (Data from 2016-01-01 to 2016-12-31)'
  download_url: https://data.humdata.org/dataset/e10e47e9-b757-4a10-8940-5ee752d4442b/resource/62de32b4-b7a9-4727-b746-a646f1b2caec/download/twn_fpanv_m_gdo_20160101_20161221_t.zip
  format: null
  id: resource_62de32b4
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: twn_fpanv_m_gdo_20160101_20161221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Taiwan (Province of China): Copernicus Vegetation Index Anomaly (FAPAR
    Anomaly) (Data from 2015-01-01 to 2015-12-31)'
  download_url: https://data.humdata.org/dataset/e10e47e9-b757-4a10-8940-5ee752d4442b/resource/b74e72ea-dd2f-4303-bcb1-885368761063/download/twn_fpanv_m_gdo_20150101_20151221_t.zip
  format: null
  id: resource_b74e72ea
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: twn_fpanv_m_gdo_20150101_20151221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Taiwan (Province of China): Copernicus Vegetation Index Anomaly (FAPAR
    Anomaly) (Data from 2014-01-01 to 2014-12-31)'
  download_url: https://data.humdata.org/dataset/e10e47e9-b757-4a10-8940-5ee752d4442b/resource/51cc29dc-8f32-4495-ae8c-3e5eb378278d/download/twn_fpanv_m_gdo_20140101_20141221_t.zip
  format: null
  id: resource_51cc29dc
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: twn_fpanv_m_gdo_20140101_20141221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Taiwan (Province of China): Copernicus Vegetation Index Anomaly (FAPAR
    Anomaly) (Data from 2013-01-01 to 2013-12-31)'
  download_url: https://data.humdata.org/dataset/e10e47e9-b757-4a10-8940-5ee752d4442b/resource/6a657cc8-c59d-4177-bf6e-f1a014488eae/download/twn_fpanv_m_gdo_20130101_20131221_t.zip
  format: null
  id: resource_6a657cc8
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: twn_fpanv_m_gdo_20130101_20131221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Taiwan (Province of China): Copernicus Vegetation Index Anomaly (FAPAR
    Anomaly) (Data from 2012-01-21 to 2012-12-31)'
  download_url: https://data.humdata.org/dataset/e10e47e9-b757-4a10-8940-5ee752d4442b/resource/3d672cff-6e44-446a-9344-99cd4ae081c3/download/twn_fpanv_m_gdo_20120121_20121221_t.zip
  format: null
  id: resource_3d672cff
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: twn_fpanv_m_gdo_20120121_20121221_t.zip
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-twn_copernicus_provincechinavegetationin_2012
spatial:
  bbox: null
  centroid: null
  countries:
  - TWN
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2026-01-10'
  start: '2012-01-21'
temporal_resolution: null
title: 'Taiwan (Province of China): Copernicus Vegetation Index Anomaly (FAPAR Anomaly)'
version: null
vulnerability: null
---
