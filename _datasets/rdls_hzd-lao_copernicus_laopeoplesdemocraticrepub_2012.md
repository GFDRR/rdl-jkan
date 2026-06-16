---
attributions:
- entity:
    affiliation: null
    email: null
    name: European Commission, Joint Research Centre (JRC)
    url: https://data.humdata.org/dataset/lao-anomalies-fapar-viirs
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Copernicus
  url: https://data.humdata.org/dataset/lao-anomalies-fapar-viirs
creator:
  affiliation: null
  email: null
  name: Copernicus
  url: https://data.humdata.org/dataset/lao-anomalies-fapar-viirs
dataset_id: rdls_hzd-lao_copernicus_laopeoplesdemocraticrepub_2012
description: 'Fraction of Absorbed Photosynthetically Active Radiation (FAPAR) is
  a biophysical dimensionless quantity (its values range from 0/no absorption to 1/total
  absorption) used to assess the greenness and health of vegetation. FAPAR anomalies
  can be used as an indicator to detect and monitor the impacts of agricultural drought
  on the growth and productivity of vegetation. The data is presented in 10-day time
  composite of the Visible Infrared Imaging Radiometer Suite (VIIRS).. [Source: This
  metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/lao-anomalies-fapar-viirs]'
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
  description: FAPAR values from VIIRS satellite observations are processed into 10-day
    temporal composites. Anomalies are calculated at each grid cell by computing the
    deviation of FAPAR from a long-term mean baseline (2012 to most recent full year),
    enabling detection and monitoring of agricultural drought impacts on vegetation
    productivity across Lao PDR.
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
- href: https://data.humdata.org/dataset/lao-anomalies-fapar-viirs
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
  description: 'Lao People''s Democratic Republic: Copernicus Vegetation Index Anomaly
    (FAPAR Anomaly) (Data from 2026-01-01 to 2026-01-10)'
  download_url: https://data.humdata.org/dataset/93c7ee5e-68f4-4a78-b69e-2eca3b783303/resource/3e634f2a-ce17-46a2-97fc-2f3e55cc2fcc/download/lao_fpanv_m_gdo_20260101_20260101_t.zip
  format: null
  id: resource_3e634f2a
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: lao_fpanv_m_gdo_20260101_20260101_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Lao People''s Democratic Republic: Copernicus Vegetation Index Anomaly
    (FAPAR Anomaly) (Data from 2025-01-01 to 2025-12-31)'
  download_url: https://data.humdata.org/dataset/93c7ee5e-68f4-4a78-b69e-2eca3b783303/resource/2777856f-68ab-4237-af48-ed1428d6af45/download/lao_fpanv_m_gdo_20250101_20251221_t.zip
  format: null
  id: resource_2777856f
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: lao_fpanv_m_gdo_20250101_20251221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Lao People''s Democratic Republic: Copernicus Vegetation Index Anomaly
    (FAPAR Anomaly) (Data from 2024-01-01 to 2024-12-31)'
  download_url: https://data.humdata.org/dataset/93c7ee5e-68f4-4a78-b69e-2eca3b783303/resource/52407db0-15dc-48d5-a40d-ddd8b712d36f/download/lao_fpanv_m_gdo_20240101_20241221_t.zip
  format: null
  id: resource_52407db0
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: lao_fpanv_m_gdo_20240101_20241221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Lao People''s Democratic Republic: Copernicus Vegetation Index Anomaly
    (FAPAR Anomaly) (Data from 2023-01-01 to 2023-12-31)'
  download_url: https://data.humdata.org/dataset/93c7ee5e-68f4-4a78-b69e-2eca3b783303/resource/355bae0e-8689-426a-849b-0c9208768f89/download/lao_fpanv_m_gdo_20230101_20231221_t.zip
  format: null
  id: resource_355bae0e
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: lao_fpanv_m_gdo_20230101_20231221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Lao People''s Democratic Republic: Copernicus Vegetation Index Anomaly
    (FAPAR Anomaly) (Data from 2022-01-01 to 2022-12-31)'
  download_url: https://data.humdata.org/dataset/93c7ee5e-68f4-4a78-b69e-2eca3b783303/resource/83fe07f9-6f32-4a63-80f5-d0ae609cc9f1/download/lao_fpanv_m_gdo_20220101_20221221_t.zip
  format: null
  id: resource_83fe07f9
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: lao_fpanv_m_gdo_20220101_20221221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Lao People''s Democratic Republic: Copernicus Vegetation Index Anomaly
    (FAPAR Anomaly) (Data from 2021-01-01 to 2021-12-31)'
  download_url: https://data.humdata.org/dataset/93c7ee5e-68f4-4a78-b69e-2eca3b783303/resource/1ae28a59-95bd-4286-8fd2-a361cf1e6dbd/download/lao_fpanv_m_gdo_20210101_20211221_t.zip
  format: null
  id: resource_1ae28a59
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: lao_fpanv_m_gdo_20210101_20211221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Lao People''s Democratic Republic: Copernicus Vegetation Index Anomaly
    (FAPAR Anomaly) (Data from 2020-01-01 to 2020-12-31)'
  download_url: https://data.humdata.org/dataset/93c7ee5e-68f4-4a78-b69e-2eca3b783303/resource/a0ca044b-691c-44b1-9e40-4d56ef2ea735/download/lao_fpanv_m_gdo_20200101_20201221_t.zip
  format: null
  id: resource_a0ca044b
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: lao_fpanv_m_gdo_20200101_20201221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Lao People''s Democratic Republic: Copernicus Vegetation Index Anomaly
    (FAPAR Anomaly) (Data from 2019-01-01 to 2019-12-31)'
  download_url: https://data.humdata.org/dataset/93c7ee5e-68f4-4a78-b69e-2eca3b783303/resource/87817684-bb5a-4212-a81e-ff06b143d7fd/download/lao_fpanv_m_gdo_20190101_20191221_t.zip
  format: null
  id: resource_87817684
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: lao_fpanv_m_gdo_20190101_20191221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Lao People''s Democratic Republic: Copernicus Vegetation Index Anomaly
    (FAPAR Anomaly) (Data from 2018-01-01 to 2018-12-31)'
  download_url: https://data.humdata.org/dataset/93c7ee5e-68f4-4a78-b69e-2eca3b783303/resource/b8de4b2d-63b0-401a-866b-9955c8ba056e/download/lao_fpanv_m_gdo_20180101_20181221_t.zip
  format: null
  id: resource_b8de4b2d
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: lao_fpanv_m_gdo_20180101_20181221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Lao People''s Democratic Republic: Copernicus Vegetation Index Anomaly
    (FAPAR Anomaly) (Data from 2017-01-01 to 2017-12-31)'
  download_url: https://data.humdata.org/dataset/93c7ee5e-68f4-4a78-b69e-2eca3b783303/resource/360f86f9-ea3a-49f4-a02a-90f166cd5bd4/download/lao_fpanv_m_gdo_20170101_20171221_t.zip
  format: null
  id: resource_360f86f9
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: lao_fpanv_m_gdo_20170101_20171221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Lao People''s Democratic Republic: Copernicus Vegetation Index Anomaly
    (FAPAR Anomaly) (Data from 2016-01-01 to 2016-12-31)'
  download_url: https://data.humdata.org/dataset/93c7ee5e-68f4-4a78-b69e-2eca3b783303/resource/126d60f7-070e-4ef2-8d2d-30e135d6e21f/download/lao_fpanv_m_gdo_20160101_20161221_t.zip
  format: null
  id: resource_126d60f7
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: lao_fpanv_m_gdo_20160101_20161221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Lao People''s Democratic Republic: Copernicus Vegetation Index Anomaly
    (FAPAR Anomaly) (Data from 2015-01-01 to 2015-12-31)'
  download_url: https://data.humdata.org/dataset/93c7ee5e-68f4-4a78-b69e-2eca3b783303/resource/777d9720-677a-4dea-a18a-c587efb3ffdf/download/lao_fpanv_m_gdo_20150101_20151221_t.zip
  format: null
  id: resource_777d9720
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: lao_fpanv_m_gdo_20150101_20151221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Lao People''s Democratic Republic: Copernicus Vegetation Index Anomaly
    (FAPAR Anomaly) (Data from 2014-01-01 to 2014-12-31)'
  download_url: https://data.humdata.org/dataset/93c7ee5e-68f4-4a78-b69e-2eca3b783303/resource/e9a22e8b-836b-499a-9c06-b83a631e3e65/download/lao_fpanv_m_gdo_20140101_20141221_t.zip
  format: null
  id: resource_e9a22e8b
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: lao_fpanv_m_gdo_20140101_20141221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Lao People''s Democratic Republic: Copernicus Vegetation Index Anomaly
    (FAPAR Anomaly) (Data from 2013-01-01 to 2013-12-31)'
  download_url: https://data.humdata.org/dataset/93c7ee5e-68f4-4a78-b69e-2eca3b783303/resource/07988498-4f64-44d9-82c5-acd8b5e42cce/download/lao_fpanv_m_gdo_20130101_20131221_t.zip
  format: null
  id: resource_07988498
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: lao_fpanv_m_gdo_20130101_20131221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Lao People''s Democratic Republic: Copernicus Vegetation Index Anomaly
    (FAPAR Anomaly) (Data from 2012-01-21 to 2012-12-31)'
  download_url: https://data.humdata.org/dataset/93c7ee5e-68f4-4a78-b69e-2eca3b783303/resource/401c9b7f-311e-4725-819b-c9c2c426d7fb/download/lao_fpanv_m_gdo_20120121_20121221_t.zip
  format: null
  id: resource_401c9b7f
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: lao_fpanv_m_gdo_20120121_20121221_t.zip
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-lao_copernicus_laopeoplesdemocraticrepub_2012
spatial:
  bbox: null
  centroid: null
  countries:
  - LAO
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2026-01-10'
  start: '2012-01-21'
temporal_resolution: null
title: 'Lao People''s Democratic Republic: Copernicus Vegetation Index Anomaly (FAPAR
  Anomaly)'
version: null
vulnerability: null
---
