---
attributions:
- entity:
    affiliation: null
    email: null
    name: Copernicus Vegetation Index (VIIRS)
    url: https://data.humdata.org/dataset/cck-anomalies-fapar-viirs
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: European Commission, Joint Research Centre (JRC)
    url: https://data.humdata.org/dataset/cck-anomalies-fapar-viirs
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Copernicus
  url: https://data.humdata.org/dataset/cck-anomalies-fapar-viirs
creator:
  affiliation: null
  email: null
  name: Copernicus
  url: https://data.humdata.org/dataset/cck-anomalies-fapar-viirs
dataset_id: rdls_hzd-cck_copernicus_cocoskeelingislandsvegeta_2012
description: 'Fraction of Absorbed Photosynthetically Active Radiation (FAPAR) is
  a biophysical dimensionless quantity (its values range from 0/no absorption to 1/total
  absorption) used to assess the greenness and health of vegetation. FAPAR anomalies
  can be used as an indicator to detect and monitor the impacts of agricultural drought
  on the growth and productivity of vegetation. The data is presented in 10-day time
  composite of the Visible Infrared Imaging Radiometer Suite (VIIRS).. [Source: This
  metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/cck-anomalies-fapar-viirs]'
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
    intervals and processed into raster composites. Anomalies are calculated at each
    grid cell as the deviation from a long-term mean baseline (2012 to the last available
    full year), enabling detection and monitoring of agricultural drought impacts
    on vegetation productivity across the Cocos (Keeling) Islands.
  sources:
  - id: source_1
    license: null
    name: Copernicus Vegetation Index (VIIRS)
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
  - id: source_2
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
- href: https://data.humdata.org/dataset/cck-anomalies-fapar-viirs
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
  description: 'Cocos (Keeling) Islands: Copernicus Vegetation Index Anomaly (FAPAR
    Anomaly) (Data from 2026-01-01 to 2026-01-10)'
  download_url: https://data.humdata.org/dataset/980844dd-34e5-40f0-bd9c-bd157222a920/resource/f813c12c-9383-475b-bc08-12bdba2655ac/download/cck_fpanv_m_gdo_20260101_20260101_t.zip
  format: null
  id: resource_f813c12c
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: cck_fpanv_m_gdo_20260101_20260101_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Cocos (Keeling) Islands: Copernicus Vegetation Index Anomaly (FAPAR
    Anomaly) (Data from 2025-01-01 to 2025-12-31)'
  download_url: https://data.humdata.org/dataset/980844dd-34e5-40f0-bd9c-bd157222a920/resource/3b31264c-1048-4cfe-ba1d-bdcd436e0030/download/cck_fpanv_m_gdo_20250101_20251221_t.zip
  format: null
  id: resource_3b31264c
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: cck_fpanv_m_gdo_20250101_20251221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Cocos (Keeling) Islands: Copernicus Vegetation Index Anomaly (FAPAR
    Anomaly) (Data from 2024-01-01 to 2024-12-31)'
  download_url: https://data.humdata.org/dataset/980844dd-34e5-40f0-bd9c-bd157222a920/resource/a572cee7-e9dd-4b29-9c21-be49347c35f2/download/cck_fpanv_m_gdo_20240101_20241221_t.zip
  format: null
  id: resource_a572cee7
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: cck_fpanv_m_gdo_20240101_20241221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Cocos (Keeling) Islands: Copernicus Vegetation Index Anomaly (FAPAR
    Anomaly) (Data from 2023-01-01 to 2023-12-31)'
  download_url: https://data.humdata.org/dataset/980844dd-34e5-40f0-bd9c-bd157222a920/resource/1f489f30-c392-484f-86c9-0602651a24af/download/cck_fpanv_m_gdo_20230101_20231221_t.zip
  format: null
  id: resource_1f489f30
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: cck_fpanv_m_gdo_20230101_20231221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Cocos (Keeling) Islands: Copernicus Vegetation Index Anomaly (FAPAR
    Anomaly) (Data from 2022-01-01 to 2022-12-31)'
  download_url: https://data.humdata.org/dataset/980844dd-34e5-40f0-bd9c-bd157222a920/resource/52ae59d4-c360-43c6-83b9-daed152e8c22/download/cck_fpanv_m_gdo_20220101_20221221_t.zip
  format: null
  id: resource_52ae59d4
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: cck_fpanv_m_gdo_20220101_20221221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Cocos (Keeling) Islands: Copernicus Vegetation Index Anomaly (FAPAR
    Anomaly) (Data from 2021-01-01 to 2021-12-31)'
  download_url: https://data.humdata.org/dataset/980844dd-34e5-40f0-bd9c-bd157222a920/resource/2b0406e5-b36f-413f-8f67-914e40ed0319/download/cck_fpanv_m_gdo_20210101_20211221_t.zip
  format: null
  id: resource_2b0406e5
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: cck_fpanv_m_gdo_20210101_20211221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Cocos (Keeling) Islands: Copernicus Vegetation Index Anomaly (FAPAR
    Anomaly) (Data from 2020-01-01 to 2020-12-31)'
  download_url: https://data.humdata.org/dataset/980844dd-34e5-40f0-bd9c-bd157222a920/resource/05528431-d4aa-4cf0-bfaf-db96d1112740/download/cck_fpanv_m_gdo_20200101_20201221_t.zip
  format: null
  id: resource_05528431
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: cck_fpanv_m_gdo_20200101_20201221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Cocos (Keeling) Islands: Copernicus Vegetation Index Anomaly (FAPAR
    Anomaly) (Data from 2019-01-01 to 2019-12-31)'
  download_url: https://data.humdata.org/dataset/980844dd-34e5-40f0-bd9c-bd157222a920/resource/66f18c97-d3f5-4bad-9494-7a899909ce16/download/cck_fpanv_m_gdo_20190101_20191221_t.zip
  format: null
  id: resource_66f18c97
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: cck_fpanv_m_gdo_20190101_20191221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Cocos (Keeling) Islands: Copernicus Vegetation Index Anomaly (FAPAR
    Anomaly) (Data from 2018-01-01 to 2018-12-31)'
  download_url: https://data.humdata.org/dataset/980844dd-34e5-40f0-bd9c-bd157222a920/resource/52aaeeba-f850-425f-b050-0c37a844748c/download/cck_fpanv_m_gdo_20180101_20181221_t.zip
  format: null
  id: resource_52aaeeba
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: cck_fpanv_m_gdo_20180101_20181221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Cocos (Keeling) Islands: Copernicus Vegetation Index Anomaly (FAPAR
    Anomaly) (Data from 2017-01-01 to 2017-12-31)'
  download_url: https://data.humdata.org/dataset/980844dd-34e5-40f0-bd9c-bd157222a920/resource/424fe16b-3c0e-4dce-9ede-fbc92aca7d5a/download/cck_fpanv_m_gdo_20170101_20171221_t.zip
  format: null
  id: resource_424fe16b
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: cck_fpanv_m_gdo_20170101_20171221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Cocos (Keeling) Islands: Copernicus Vegetation Index Anomaly (FAPAR
    Anomaly) (Data from 2016-01-01 to 2016-12-31)'
  download_url: https://data.humdata.org/dataset/980844dd-34e5-40f0-bd9c-bd157222a920/resource/34921e61-6e34-42d1-9c71-95b281dcc9a9/download/cck_fpanv_m_gdo_20160101_20161221_t.zip
  format: null
  id: resource_34921e61
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: cck_fpanv_m_gdo_20160101_20161221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Cocos (Keeling) Islands: Copernicus Vegetation Index Anomaly (FAPAR
    Anomaly) (Data from 2015-01-01 to 2015-12-31)'
  download_url: https://data.humdata.org/dataset/980844dd-34e5-40f0-bd9c-bd157222a920/resource/1e20c719-277d-424d-b321-e1f6ff1d0d13/download/cck_fpanv_m_gdo_20150101_20151221_t.zip
  format: null
  id: resource_1e20c719
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: cck_fpanv_m_gdo_20150101_20151221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Cocos (Keeling) Islands: Copernicus Vegetation Index Anomaly (FAPAR
    Anomaly) (Data from 2014-01-01 to 2014-12-31)'
  download_url: https://data.humdata.org/dataset/980844dd-34e5-40f0-bd9c-bd157222a920/resource/c815f311-577b-4f74-afac-e65c76314cf3/download/cck_fpanv_m_gdo_20140101_20141221_t.zip
  format: null
  id: resource_c815f311
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: cck_fpanv_m_gdo_20140101_20141221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Cocos (Keeling) Islands: Copernicus Vegetation Index Anomaly (FAPAR
    Anomaly) (Data from 2013-01-01 to 2013-12-31)'
  download_url: https://data.humdata.org/dataset/980844dd-34e5-40f0-bd9c-bd157222a920/resource/9142ded5-195a-48db-afee-b909594f9376/download/cck_fpanv_m_gdo_20130101_20131221_t.zip
  format: null
  id: resource_9142ded5
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: cck_fpanv_m_gdo_20130101_20131221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Cocos (Keeling) Islands: Copernicus Vegetation Index Anomaly (FAPAR
    Anomaly) (Data from 2012-01-21 to 2012-12-31)'
  download_url: https://data.humdata.org/dataset/980844dd-34e5-40f0-bd9c-bd157222a920/resource/213bcfe8-cc17-4f1f-a67c-c4bebe1eec57/download/cck_fpanv_m_gdo_20120121_20121221_t.zip
  format: null
  id: resource_213bcfe8
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: cck_fpanv_m_gdo_20120121_20121221_t.zip
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-cck_copernicus_cocoskeelingislandsvegeta_2012
spatial:
  bbox: null
  centroid: null
  countries:
  - CCK
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2026-01-10'
  start: '2012-01-21'
temporal_resolution: null
title: 'Cocos (Keeling) Islands: Copernicus Vegetation Index Anomaly (FAPAR Anomaly)'
version: null
vulnerability: null
---
