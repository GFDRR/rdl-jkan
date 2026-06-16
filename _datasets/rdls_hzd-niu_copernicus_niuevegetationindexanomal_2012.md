---
attributions:
- entity:
    affiliation: null
    email: null
    name: European Commission, Joint Research Centre (JRC)
    url: https://data.humdata.org/dataset/niu-anomalies-fapar-viirs
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Copernicus
  url: https://data.humdata.org/dataset/niu-anomalies-fapar-viirs
creator:
  affiliation: null
  email: null
  name: Copernicus
  url: https://data.humdata.org/dataset/niu-anomalies-fapar-viirs
dataset_id: rdls_hzd-niu_copernicus_niuevegetationindexanomal_2012
description: 'Fraction of Absorbed Photosynthetically Active Radiation (FAPAR) is
  a biophysical dimensionless quantity (its values range from 0/no absorption to 1/total
  absorption) used to assess the greenness and health of vegetation. FAPAR anomalies
  can be used as an indicator to detect and monitor the impacts of agricultural drought
  on the growth and productivity of vegetation. The data is presented in 10-day time
  composite of the Visible Infrared Imaging Radiometer Suite (VIIRS).. [Source: This
  metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/niu-anomalies-fapar-viirs]'
details: Variations in the vegetation health and/or cover could be related to stress
  factors not related to droughts (e.g., plant diseases, pests, hail, flooding). To
  determine if changes in FAPAR are linked with a drought event or not, FAPAR data
  should be interpreted jointly with other indicators (as in the EDO Combined Drought
  Indicator).
exposure: []
hazard:
  event_sets_by_hazard_type:
    drought:
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
  event_sets_count: 1
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: FAPAR values derived from VIIRS satellite observations are processed
    into 10-day temporal composites. Anomalies are calculated at each grid cell by
    computing the deviation from a long-term mean baseline (2012 to the last available
    full year), enabling detection and monitoring of agricultural drought impacts
    on vegetation productivity across Niue.
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
- href: https://data.humdata.org/dataset/niu-anomalies-fapar-viirs
  rel: source
loss:
  losses: []
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
  description: 'Niue: Copernicus Vegetation Index Anomaly (FAPAR Anomaly) (Data from
    2026-01-01 to 2026-01-10)'
  download_url: https://data.humdata.org/dataset/d8050b33-ee90-48e2-a4d7-a945acda1ae4/resource/59f24d84-57bb-4219-a906-88a5ab2619f6/download/niu_fpanv_m_gdo_20260101_20260101_t.zip
  format: null
  id: resource_59f24d84
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: niu_fpanv_m_gdo_20260101_20260101_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Niue: Copernicus Vegetation Index Anomaly (FAPAR Anomaly) (Data from
    2025-01-01 to 2025-12-31)'
  download_url: https://data.humdata.org/dataset/d8050b33-ee90-48e2-a4d7-a945acda1ae4/resource/a020b743-5bd8-40ae-ac1d-2033a37ad14f/download/niu_fpanv_m_gdo_20250101_20251221_t.zip
  format: null
  id: resource_a020b743
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: niu_fpanv_m_gdo_20250101_20251221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Niue: Copernicus Vegetation Index Anomaly (FAPAR Anomaly) (Data from
    2024-01-01 to 2024-12-31)'
  download_url: https://data.humdata.org/dataset/d8050b33-ee90-48e2-a4d7-a945acda1ae4/resource/3735c4fa-71c9-4e86-9762-fd12d3aba108/download/niu_fpanv_m_gdo_20240101_20241221_t.zip
  format: null
  id: resource_3735c4fa
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: niu_fpanv_m_gdo_20240101_20241221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Niue: Copernicus Vegetation Index Anomaly (FAPAR Anomaly) (Data from
    2023-01-01 to 2023-12-31)'
  download_url: https://data.humdata.org/dataset/d8050b33-ee90-48e2-a4d7-a945acda1ae4/resource/4ea4fdf4-a05e-4a40-b698-f9c0c63b193c/download/niu_fpanv_m_gdo_20230101_20231221_t.zip
  format: null
  id: resource_4ea4fdf4
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: niu_fpanv_m_gdo_20230101_20231221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Niue: Copernicus Vegetation Index Anomaly (FAPAR Anomaly) (Data from
    2022-01-01 to 2022-12-31)'
  download_url: https://data.humdata.org/dataset/d8050b33-ee90-48e2-a4d7-a945acda1ae4/resource/2ee93b89-674c-4fc7-b286-f480c3b9cd12/download/niu_fpanv_m_gdo_20220101_20221221_t.zip
  format: null
  id: resource_2ee93b89
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: niu_fpanv_m_gdo_20220101_20221221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Niue: Copernicus Vegetation Index Anomaly (FAPAR Anomaly) (Data from
    2021-01-01 to 2021-12-31)'
  download_url: https://data.humdata.org/dataset/d8050b33-ee90-48e2-a4d7-a945acda1ae4/resource/beaa4b61-6f84-4dc9-877b-f5d24a855dc1/download/niu_fpanv_m_gdo_20210101_20211221_t.zip
  format: null
  id: resource_beaa4b61
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: niu_fpanv_m_gdo_20210101_20211221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Niue: Copernicus Vegetation Index Anomaly (FAPAR Anomaly) (Data from
    2020-01-01 to 2020-12-31)'
  download_url: https://data.humdata.org/dataset/d8050b33-ee90-48e2-a4d7-a945acda1ae4/resource/7fdd5524-52e0-4bd5-a4f8-f37d4455456d/download/niu_fpanv_m_gdo_20200101_20201221_t.zip
  format: null
  id: resource_7fdd5524
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: niu_fpanv_m_gdo_20200101_20201221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Niue: Copernicus Vegetation Index Anomaly (FAPAR Anomaly) (Data from
    2019-01-01 to 2019-12-31)'
  download_url: https://data.humdata.org/dataset/d8050b33-ee90-48e2-a4d7-a945acda1ae4/resource/3ced7fb5-879d-4b35-b8ff-96a4b370d695/download/niu_fpanv_m_gdo_20190101_20191221_t.zip
  format: null
  id: resource_3ced7fb5
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: niu_fpanv_m_gdo_20190101_20191221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Niue: Copernicus Vegetation Index Anomaly (FAPAR Anomaly) (Data from
    2018-01-01 to 2018-12-31)'
  download_url: https://data.humdata.org/dataset/d8050b33-ee90-48e2-a4d7-a945acda1ae4/resource/80ae432e-5160-466b-b7b9-2734de7df673/download/niu_fpanv_m_gdo_20180101_20181221_t.zip
  format: null
  id: resource_80ae432e
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: niu_fpanv_m_gdo_20180101_20181221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Niue: Copernicus Vegetation Index Anomaly (FAPAR Anomaly) (Data from
    2017-01-01 to 2017-12-31)'
  download_url: https://data.humdata.org/dataset/d8050b33-ee90-48e2-a4d7-a945acda1ae4/resource/c95daf17-d7b1-4898-b783-842b8ea52a97/download/niu_fpanv_m_gdo_20170101_20171221_t.zip
  format: null
  id: resource_c95daf17
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: niu_fpanv_m_gdo_20170101_20171221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Niue: Copernicus Vegetation Index Anomaly (FAPAR Anomaly) (Data from
    2016-01-01 to 2016-12-31)'
  download_url: https://data.humdata.org/dataset/d8050b33-ee90-48e2-a4d7-a945acda1ae4/resource/d3a073ea-9e91-48f5-8151-d232aa311480/download/niu_fpanv_m_gdo_20160101_20161221_t.zip
  format: null
  id: resource_d3a073ea
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: niu_fpanv_m_gdo_20160101_20161221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Niue: Copernicus Vegetation Index Anomaly (FAPAR Anomaly) (Data from
    2015-01-01 to 2015-12-31)'
  download_url: https://data.humdata.org/dataset/d8050b33-ee90-48e2-a4d7-a945acda1ae4/resource/f9e49de6-b912-4a18-b393-20b927e26bde/download/niu_fpanv_m_gdo_20150101_20151221_t.zip
  format: null
  id: resource_f9e49de6
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: niu_fpanv_m_gdo_20150101_20151221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Niue: Copernicus Vegetation Index Anomaly (FAPAR Anomaly) (Data from
    2014-01-01 to 2014-12-31)'
  download_url: https://data.humdata.org/dataset/d8050b33-ee90-48e2-a4d7-a945acda1ae4/resource/8b187b5d-4ecb-46f4-aabc-f72de1dc7793/download/niu_fpanv_m_gdo_20140101_20141221_t.zip
  format: null
  id: resource_8b187b5d
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: niu_fpanv_m_gdo_20140101_20141221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Niue: Copernicus Vegetation Index Anomaly (FAPAR Anomaly) (Data from
    2013-01-01 to 2013-12-31)'
  download_url: https://data.humdata.org/dataset/d8050b33-ee90-48e2-a4d7-a945acda1ae4/resource/f4ae1796-b560-47bc-b6ac-3a74ef88442f/download/niu_fpanv_m_gdo_20130101_20131221_t.zip
  format: null
  id: resource_f4ae1796
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: niu_fpanv_m_gdo_20130101_20131221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Niue: Copernicus Vegetation Index Anomaly (FAPAR Anomaly) (Data from
    2012-01-21 to 2012-12-31)'
  download_url: https://data.humdata.org/dataset/d8050b33-ee90-48e2-a4d7-a945acda1ae4/resource/79df409d-1275-4151-ace0-292078344b88/download/niu_fpanv_m_gdo_20120121_20121221_t.zip
  format: null
  id: resource_79df409d
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: niu_fpanv_m_gdo_20120121_20121221_t.zip
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-niu_copernicus_niuevegetationindexanomal_2012
spatial:
  bbox: null
  centroid: null
  countries:
  - NIU
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2026-01-10'
  start: '2012-01-21'
temporal_resolution: null
title: 'Niue: Copernicus Vegetation Index Anomaly (FAPAR Anomaly)'
version: null
vulnerability: null
---
