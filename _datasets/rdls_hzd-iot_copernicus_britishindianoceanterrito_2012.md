---
attributions:
- entity:
    affiliation: null
    email: null
    name: European Commission, Joint Research Centre (JRC)
    url: https://data.humdata.org/dataset/iot-anomalies-fapar-viirs
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Copernicus
  url: https://data.humdata.org/dataset/iot-anomalies-fapar-viirs
creator:
  affiliation: null
  email: null
  name: Copernicus
  url: https://data.humdata.org/dataset/iot-anomalies-fapar-viirs
dataset_id: rdls_hzd-iot_copernicus_britishindianoceanterrito_2012
description: 'Fraction of Absorbed Photosynthetically Active Radiation (FAPAR) is
  a biophysical dimensionless quantity (its values range from 0/no absorption to 1/total
  absorption) used to assess the greenness and health of vegetation. FAPAR anomalies
  can be used as an indicator to detect and monitor the impacts of agricultural drought
  on the growth and productivity of vegetation. The data is presented in 10-day time
  composite of the Visible Infrared Imaging Radiometer Suite (VIIRS).. [Source: This
  metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/iot-anomalies-fapar-viirs]'
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
  event_sets_count: 1
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: FAPAR values from VIIRS satellite observations are collected at 10-day
    intervals. Anomalies are calculated at each grid cell by computing the deviation
    of FAPAR from a long-term mean baseline spanning 2012 to the most recent complete
    year, enabling detection and monitoring of agricultural drought impacts on vegetation
    productivity.
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
- href: https://data.humdata.org/dataset/iot-anomalies-fapar-viirs
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
  description: 'British Indian Ocean Territory: Copernicus Vegetation Index Anomaly
    (FAPAR Anomaly) (Data from 2026-01-01 to 2026-01-10)'
  download_url: https://data.humdata.org/dataset/eb5c3b33-9895-40c4-b65c-6f457468777d/resource/beeb80eb-3924-457c-8a1b-84fe79d44e4c/download/iot_fpanv_m_gdo_20260101_20260101_t.zip
  format: null
  id: resource_beeb80eb
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: iot_fpanv_m_gdo_20260101_20260101_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'British Indian Ocean Territory: Copernicus Vegetation Index Anomaly
    (FAPAR Anomaly) (Data from 2025-01-01 to 2025-12-31)'
  download_url: https://data.humdata.org/dataset/eb5c3b33-9895-40c4-b65c-6f457468777d/resource/ec299363-6ffc-455b-aa25-0edbd258e145/download/iot_fpanv_m_gdo_20250101_20251221_t.zip
  format: null
  id: resource_ec299363
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: iot_fpanv_m_gdo_20250101_20251221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'British Indian Ocean Territory: Copernicus Vegetation Index Anomaly
    (FAPAR Anomaly) (Data from 2024-01-01 to 2024-12-31)'
  download_url: https://data.humdata.org/dataset/eb5c3b33-9895-40c4-b65c-6f457468777d/resource/d57acda3-28b2-439e-b77e-4634f3b00f8e/download/iot_fpanv_m_gdo_20240101_20241221_t.zip
  format: null
  id: resource_d57acda3
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: iot_fpanv_m_gdo_20240101_20241221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'British Indian Ocean Territory: Copernicus Vegetation Index Anomaly
    (FAPAR Anomaly) (Data from 2023-01-01 to 2023-12-31)'
  download_url: https://data.humdata.org/dataset/eb5c3b33-9895-40c4-b65c-6f457468777d/resource/f7e5421a-520c-4857-833b-0dd93c6b2d41/download/iot_fpanv_m_gdo_20230101_20231221_t.zip
  format: null
  id: resource_f7e5421a
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: iot_fpanv_m_gdo_20230101_20231221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'British Indian Ocean Territory: Copernicus Vegetation Index Anomaly
    (FAPAR Anomaly) (Data from 2022-01-01 to 2022-12-31)'
  download_url: https://data.humdata.org/dataset/eb5c3b33-9895-40c4-b65c-6f457468777d/resource/d2d5076d-1b2e-49c2-a688-031917580352/download/iot_fpanv_m_gdo_20220101_20221221_t.zip
  format: null
  id: resource_d2d5076d
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: iot_fpanv_m_gdo_20220101_20221221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'British Indian Ocean Territory: Copernicus Vegetation Index Anomaly
    (FAPAR Anomaly) (Data from 2021-01-01 to 2021-12-31)'
  download_url: https://data.humdata.org/dataset/eb5c3b33-9895-40c4-b65c-6f457468777d/resource/8681c231-f211-4d18-befe-1d3017e15969/download/iot_fpanv_m_gdo_20210101_20211221_t.zip
  format: null
  id: resource_8681c231
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: iot_fpanv_m_gdo_20210101_20211221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'British Indian Ocean Territory: Copernicus Vegetation Index Anomaly
    (FAPAR Anomaly) (Data from 2020-01-01 to 2020-12-31)'
  download_url: https://data.humdata.org/dataset/eb5c3b33-9895-40c4-b65c-6f457468777d/resource/73e98a01-9886-4e3b-a4ad-a7a939cbf1f0/download/iot_fpanv_m_gdo_20200101_20201221_t.zip
  format: null
  id: resource_73e98a01
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: iot_fpanv_m_gdo_20200101_20201221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'British Indian Ocean Territory: Copernicus Vegetation Index Anomaly
    (FAPAR Anomaly) (Data from 2019-01-01 to 2019-12-31)'
  download_url: https://data.humdata.org/dataset/eb5c3b33-9895-40c4-b65c-6f457468777d/resource/f81810ff-a7df-4245-94a8-57a0d65f39e9/download/iot_fpanv_m_gdo_20190101_20191221_t.zip
  format: null
  id: resource_f81810ff
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: iot_fpanv_m_gdo_20190101_20191221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'British Indian Ocean Territory: Copernicus Vegetation Index Anomaly
    (FAPAR Anomaly) (Data from 2018-01-01 to 2018-12-31)'
  download_url: https://data.humdata.org/dataset/eb5c3b33-9895-40c4-b65c-6f457468777d/resource/f45744a9-2a50-4c3a-8c21-336132782e01/download/iot_fpanv_m_gdo_20180101_20181221_t.zip
  format: null
  id: resource_f45744a9
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: iot_fpanv_m_gdo_20180101_20181221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'British Indian Ocean Territory: Copernicus Vegetation Index Anomaly
    (FAPAR Anomaly) (Data from 2017-01-01 to 2017-12-31)'
  download_url: https://data.humdata.org/dataset/eb5c3b33-9895-40c4-b65c-6f457468777d/resource/f2711fd4-5ab0-4eac-9f8c-b3ab26aff86b/download/iot_fpanv_m_gdo_20170101_20171221_t.zip
  format: null
  id: resource_f2711fd4
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: iot_fpanv_m_gdo_20170101_20171221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'British Indian Ocean Territory: Copernicus Vegetation Index Anomaly
    (FAPAR Anomaly) (Data from 2016-01-01 to 2016-12-31)'
  download_url: https://data.humdata.org/dataset/eb5c3b33-9895-40c4-b65c-6f457468777d/resource/1e542fa2-83ab-4278-b739-a5baa658da3f/download/iot_fpanv_m_gdo_20160101_20161221_t.zip
  format: null
  id: resource_1e542fa2
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: iot_fpanv_m_gdo_20160101_20161221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'British Indian Ocean Territory: Copernicus Vegetation Index Anomaly
    (FAPAR Anomaly) (Data from 2015-01-01 to 2015-12-31)'
  download_url: https://data.humdata.org/dataset/eb5c3b33-9895-40c4-b65c-6f457468777d/resource/13cc76e9-fc2c-444e-b210-f3991c7fc410/download/iot_fpanv_m_gdo_20150101_20151221_t.zip
  format: null
  id: resource_13cc76e9
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: iot_fpanv_m_gdo_20150101_20151221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'British Indian Ocean Territory: Copernicus Vegetation Index Anomaly
    (FAPAR Anomaly) (Data from 2014-01-01 to 2014-12-31)'
  download_url: https://data.humdata.org/dataset/eb5c3b33-9895-40c4-b65c-6f457468777d/resource/b89c058f-ffee-4ad6-a7c6-a12629bbe5f2/download/iot_fpanv_m_gdo_20140101_20141221_t.zip
  format: null
  id: resource_b89c058f
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: iot_fpanv_m_gdo_20140101_20141221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'British Indian Ocean Territory: Copernicus Vegetation Index Anomaly
    (FAPAR Anomaly) (Data from 2013-01-01 to 2013-12-31)'
  download_url: https://data.humdata.org/dataset/eb5c3b33-9895-40c4-b65c-6f457468777d/resource/67f111a2-1cfc-4a96-8369-7619bf641805/download/iot_fpanv_m_gdo_20130101_20131221_t.zip
  format: null
  id: resource_67f111a2
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: iot_fpanv_m_gdo_20130101_20131221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'British Indian Ocean Territory: Copernicus Vegetation Index Anomaly
    (FAPAR Anomaly) (Data from 2012-01-21 to 2012-12-31)'
  download_url: https://data.humdata.org/dataset/eb5c3b33-9895-40c4-b65c-6f457468777d/resource/96421d73-9649-4152-a7cc-8d0ded11acd6/download/iot_fpanv_m_gdo_20120121_20121221_t.zip
  format: null
  id: resource_96421d73
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: iot_fpanv_m_gdo_20120121_20121221_t.zip
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-iot_copernicus_britishindianoceanterrito_2012
spatial:
  bbox: null
  centroid: null
  countries:
  - IOT
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2026-01-10'
  start: '2012-01-21'
temporal_resolution: null
title: 'British Indian Ocean Territory: Copernicus Vegetation Index Anomaly (FAPAR
  Anomaly)'
version: null
vulnerability: null
---
