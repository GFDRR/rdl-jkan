---
attributions:
- entity:
    affiliation: null
    email: null
    name: European Commission, Joint Research Centre (JRC)
    url: https://data.humdata.org/dataset/civ-anomalies-fapar-viirs
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Copernicus
  url: https://data.humdata.org/dataset/civ-anomalies-fapar-viirs
creator:
  affiliation: null
  email: null
  name: Copernicus
  url: https://data.humdata.org/dataset/civ-anomalies-fapar-viirs
dataset_id: rdls_hzd-civ_copernicus_vegetationindexanomalyfap_2012
description: 'Fraction of Absorbed Photosynthetically Active Radiation (FAPAR) is
  a biophysical dimensionless quantity (its values range from 0/no absorption to 1/total
  absorption) used to assess the greenness and health of vegetation. FAPAR anomalies
  can be used as an indicator to detect and monitor the impacts of agricultural drought
  on the growth and productivity of vegetation. The data is presented in 10-day time
  composite of the Visible Infrared Imaging Radiometer Suite (VIIRS).. [Source: This
  metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/civ-anomalies-fapar-viirs]'
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
  description: "FAPAR values from VIIRS satellite observations are processed into\
    \ 10-day time composites for C\xF4te d'Ivoire. Anomalies are calculated at each\
    \ grid cell as the deviation from a long-term mean baseline (2012 to the last\
    \ available full year), producing raster datasets that serve as an empirical indicator\
    \ of agricultural drought impacts on vegetation growth and productivity."
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
- href: https://data.humdata.org/dataset/civ-anomalies-fapar-viirs
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
  description: "C\xF4te d'Ivoire: Copernicus Vegetation Index Anomaly (FAPAR Anomaly)\
    \ (Data from 2026-01-01 to 2026-01-10)"
  download_url: https://data.humdata.org/dataset/60e836d6-8997-4993-9010-9b1572429f87/resource/71ec8004-c16a-43b7-bece-566bc588c54f/download/civ_fpanv_m_gdo_20260101_20260101_t.zip
  format: null
  id: resource_71ec8004
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: civ_fpanv_m_gdo_20260101_20260101_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "C\xF4te d'Ivoire: Copernicus Vegetation Index Anomaly (FAPAR Anomaly)\
    \ (Data from 2025-01-01 to 2025-12-31)"
  download_url: https://data.humdata.org/dataset/60e836d6-8997-4993-9010-9b1572429f87/resource/e24cd423-4709-403a-a5e5-848f988b7b89/download/civ_fpanv_m_gdo_20250101_20251221_t.zip
  format: null
  id: resource_e24cd423
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: civ_fpanv_m_gdo_20250101_20251221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "C\xF4te d'Ivoire: Copernicus Vegetation Index Anomaly (FAPAR Anomaly)\
    \ (Data from 2024-01-01 to 2024-12-31)"
  download_url: https://data.humdata.org/dataset/60e836d6-8997-4993-9010-9b1572429f87/resource/692f5f0b-3e3e-487a-b036-43f5bc2c76ca/download/civ_fpanv_m_gdo_20240101_20241221_t.zip
  format: null
  id: resource_692f5f0b
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: civ_fpanv_m_gdo_20240101_20241221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "C\xF4te d'Ivoire: Copernicus Vegetation Index Anomaly (FAPAR Anomaly)\
    \ (Data from 2023-01-01 to 2023-12-31)"
  download_url: https://data.humdata.org/dataset/60e836d6-8997-4993-9010-9b1572429f87/resource/06966af9-297a-4ec2-a644-a21cd953e6ba/download/civ_fpanv_m_gdo_20230101_20231221_t.zip
  format: null
  id: resource_06966af9
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: civ_fpanv_m_gdo_20230101_20231221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "C\xF4te d'Ivoire: Copernicus Vegetation Index Anomaly (FAPAR Anomaly)\
    \ (Data from 2022-01-01 to 2022-12-31)"
  download_url: https://data.humdata.org/dataset/60e836d6-8997-4993-9010-9b1572429f87/resource/ad46177d-95b2-439f-9c56-7e770d96f1aa/download/civ_fpanv_m_gdo_20220101_20221221_t.zip
  format: null
  id: resource_ad46177d
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: civ_fpanv_m_gdo_20220101_20221221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "C\xF4te d'Ivoire: Copernicus Vegetation Index Anomaly (FAPAR Anomaly)\
    \ (Data from 2021-01-01 to 2021-12-31)"
  download_url: https://data.humdata.org/dataset/60e836d6-8997-4993-9010-9b1572429f87/resource/91960940-94ce-4895-b7b9-e85c5e91615f/download/civ_fpanv_m_gdo_20210101_20211221_t.zip
  format: null
  id: resource_91960940
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: civ_fpanv_m_gdo_20210101_20211221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "C\xF4te d'Ivoire: Copernicus Vegetation Index Anomaly (FAPAR Anomaly)\
    \ (Data from 2020-01-01 to 2020-12-31)"
  download_url: https://data.humdata.org/dataset/60e836d6-8997-4993-9010-9b1572429f87/resource/072707d0-96da-417c-b743-431e5256be32/download/civ_fpanv_m_gdo_20200101_20201221_t.zip
  format: null
  id: resource_072707d0
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: civ_fpanv_m_gdo_20200101_20201221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "C\xF4te d'Ivoire: Copernicus Vegetation Index Anomaly (FAPAR Anomaly)\
    \ (Data from 2019-01-01 to 2019-12-31)"
  download_url: https://data.humdata.org/dataset/60e836d6-8997-4993-9010-9b1572429f87/resource/9b4c5138-c0b3-4b05-94a6-ce3e6a2d51b2/download/civ_fpanv_m_gdo_20190101_20191221_t.zip
  format: null
  id: resource_9b4c5138
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: civ_fpanv_m_gdo_20190101_20191221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "C\xF4te d'Ivoire: Copernicus Vegetation Index Anomaly (FAPAR Anomaly)\
    \ (Data from 2018-01-01 to 2018-12-31)"
  download_url: https://data.humdata.org/dataset/60e836d6-8997-4993-9010-9b1572429f87/resource/521cb37e-b698-40c8-ad71-ca48c1e9380f/download/civ_fpanv_m_gdo_20180101_20181221_t.zip
  format: null
  id: resource_521cb37e
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: civ_fpanv_m_gdo_20180101_20181221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "C\xF4te d'Ivoire: Copernicus Vegetation Index Anomaly (FAPAR Anomaly)\
    \ (Data from 2017-01-01 to 2017-12-31)"
  download_url: https://data.humdata.org/dataset/60e836d6-8997-4993-9010-9b1572429f87/resource/111560b3-d636-46bd-942a-2c3f481f9e13/download/civ_fpanv_m_gdo_20170101_20171221_t.zip
  format: null
  id: resource_111560b3
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: civ_fpanv_m_gdo_20170101_20171221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "C\xF4te d'Ivoire: Copernicus Vegetation Index Anomaly (FAPAR Anomaly)\
    \ (Data from 2016-01-01 to 2016-12-31)"
  download_url: https://data.humdata.org/dataset/60e836d6-8997-4993-9010-9b1572429f87/resource/b2ab8c93-af15-48ce-a9d1-021efa3b4d3d/download/civ_fpanv_m_gdo_20160101_20161221_t.zip
  format: null
  id: resource_b2ab8c93
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: civ_fpanv_m_gdo_20160101_20161221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "C\xF4te d'Ivoire: Copernicus Vegetation Index Anomaly (FAPAR Anomaly)\
    \ (Data from 2015-01-01 to 2015-12-31)"
  download_url: https://data.humdata.org/dataset/60e836d6-8997-4993-9010-9b1572429f87/resource/cda72489-3df6-4cb2-8e0d-8830286e9319/download/civ_fpanv_m_gdo_20150101_20151221_t.zip
  format: null
  id: resource_cda72489
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: civ_fpanv_m_gdo_20150101_20151221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "C\xF4te d'Ivoire: Copernicus Vegetation Index Anomaly (FAPAR Anomaly)\
    \ (Data from 2014-01-01 to 2014-12-31)"
  download_url: https://data.humdata.org/dataset/60e836d6-8997-4993-9010-9b1572429f87/resource/e511329f-9338-44ff-8c1a-f7f5babca534/download/civ_fpanv_m_gdo_20140101_20141221_t.zip
  format: null
  id: resource_e511329f
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: civ_fpanv_m_gdo_20140101_20141221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "C\xF4te d'Ivoire: Copernicus Vegetation Index Anomaly (FAPAR Anomaly)\
    \ (Data from 2013-01-01 to 2013-12-31)"
  download_url: https://data.humdata.org/dataset/60e836d6-8997-4993-9010-9b1572429f87/resource/0fda4e4f-203f-401c-b770-b2296ec1b682/download/civ_fpanv_m_gdo_20130101_20131221_t.zip
  format: null
  id: resource_0fda4e4f
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: civ_fpanv_m_gdo_20130101_20131221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "C\xF4te d'Ivoire: Copernicus Vegetation Index Anomaly (FAPAR Anomaly)\
    \ (Data from 2012-01-21 to 2012-12-31)"
  download_url: https://data.humdata.org/dataset/60e836d6-8997-4993-9010-9b1572429f87/resource/fc123d05-4aff-46f3-afd9-3789f62fd547/download/civ_fpanv_m_gdo_20120121_20121221_t.zip
  format: null
  id: resource_fc123d05
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: civ_fpanv_m_gdo_20120121_20121221_t.zip
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-civ_copernicus_vegetationindexanomalyfap_2012
spatial:
  bbox: null
  centroid: null
  countries:
  - CIV
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2026-01-10'
  start: '2012-01-21'
temporal_resolution: null
title: "C\xF4te d'Ivoire: Copernicus Vegetation Index Anomaly (FAPAR Anomaly)"
version: null
vulnerability: null
---
