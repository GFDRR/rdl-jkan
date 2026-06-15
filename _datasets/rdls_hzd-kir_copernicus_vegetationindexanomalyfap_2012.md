---
attributions:
- entity:
    affiliation: null
    email: null
    name: European Commission, Joint Research Centre (JRC)
    url: https://data.humdata.org/dataset/kir-anomalies-fapar-viirs
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Copernicus
  url: https://data.humdata.org/dataset/kir-anomalies-fapar-viirs
creator:
  affiliation: null
  email: null
  name: Copernicus
  url: https://data.humdata.org/dataset/kir-anomalies-fapar-viirs
dataset_id: rdls_hzd-kir_copernicus_vegetationindexanomalyfap_2012
description: 'Fraction of Absorbed Photosynthetically Active Radiation (FAPAR) is
  a biophysical dimensionless quantity (its values range from 0/no absorption to 1/total
  absorption) used to assess the greenness and health of vegetation. FAPAR anomalies
  can be used as an indicator to detect and monitor the impacts of agricultural drought
  on the growth and productivity of vegetation. The data is presented in 10-day time
  composite of the Visible Infrared Imaging Radiometer Suite (VIIRS).. [Source: This
  metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/kir-anomalies-fapar-viirs]'
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
  description: FAPAR values derived from VIIRS satellite observations are processed
    into 10-day temporal composites. Anomalies are calculated at each grid cell as
    the deviation from a long-term mean baseline (2012 to last available full year),
    enabling detection and monitoring of agricultural drought impacts on vegetation
    growth and productivity across Kiribati.
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
- href: https://data.humdata.org/dataset/kir-anomalies-fapar-viirs
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
  description: 'Kiribati: Copernicus Vegetation Index Anomaly (FAPAR Anomaly) (Data
    from 2026-01-01 to 2026-01-10)'
  download_url: https://data.humdata.org/dataset/29ceb0f4-49d9-4c7f-9841-aa4379d119fc/resource/e2435c61-a8bb-4776-a907-012c1169380a/download/kir_fpanv_m_gdo_20260101_20260101_t.zip
  format: null
  id: resource_e2435c61
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: kir_fpanv_m_gdo_20260101_20260101_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Kiribati: Copernicus Vegetation Index Anomaly (FAPAR Anomaly) (Data
    from 2025-01-01 to 2025-12-31)'
  download_url: https://data.humdata.org/dataset/29ceb0f4-49d9-4c7f-9841-aa4379d119fc/resource/dac47d6c-79cd-49cc-862b-6ec5526167ae/download/kir_fpanv_m_gdo_20250101_20251221_t.zip
  format: null
  id: resource_dac47d6c
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: kir_fpanv_m_gdo_20250101_20251221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Kiribati: Copernicus Vegetation Index Anomaly (FAPAR Anomaly) (Data
    from 2024-01-01 to 2024-12-31)'
  download_url: https://data.humdata.org/dataset/29ceb0f4-49d9-4c7f-9841-aa4379d119fc/resource/5001d70c-aaa2-4cab-a50d-0b708d22484c/download/kir_fpanv_m_gdo_20240101_20241221_t.zip
  format: null
  id: resource_5001d70c
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: kir_fpanv_m_gdo_20240101_20241221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Kiribati: Copernicus Vegetation Index Anomaly (FAPAR Anomaly) (Data
    from 2023-01-01 to 2023-12-31)'
  download_url: https://data.humdata.org/dataset/29ceb0f4-49d9-4c7f-9841-aa4379d119fc/resource/cc099bbe-7147-456b-8c3a-51017af261e1/download/kir_fpanv_m_gdo_20230101_20231221_t.zip
  format: null
  id: resource_cc099bbe
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: kir_fpanv_m_gdo_20230101_20231221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Kiribati: Copernicus Vegetation Index Anomaly (FAPAR Anomaly) (Data
    from 2022-01-01 to 2022-12-31)'
  download_url: https://data.humdata.org/dataset/29ceb0f4-49d9-4c7f-9841-aa4379d119fc/resource/8614833c-bf73-42d5-a114-0c4a83ad22eb/download/kir_fpanv_m_gdo_20220101_20221221_t.zip
  format: null
  id: resource_8614833c
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: kir_fpanv_m_gdo_20220101_20221221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Kiribati: Copernicus Vegetation Index Anomaly (FAPAR Anomaly) (Data
    from 2021-01-01 to 2021-12-31)'
  download_url: https://data.humdata.org/dataset/29ceb0f4-49d9-4c7f-9841-aa4379d119fc/resource/f66dcda6-a314-40f7-b532-861a9cee4302/download/kir_fpanv_m_gdo_20210101_20211221_t.zip
  format: null
  id: resource_f66dcda6
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: kir_fpanv_m_gdo_20210101_20211221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Kiribati: Copernicus Vegetation Index Anomaly (FAPAR Anomaly) (Data
    from 2020-01-01 to 2020-12-31)'
  download_url: https://data.humdata.org/dataset/29ceb0f4-49d9-4c7f-9841-aa4379d119fc/resource/1334c086-cc4a-4905-a9f7-6cdef85a8b40/download/kir_fpanv_m_gdo_20200101_20201221_t.zip
  format: null
  id: resource_1334c086
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: kir_fpanv_m_gdo_20200101_20201221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Kiribati: Copernicus Vegetation Index Anomaly (FAPAR Anomaly) (Data
    from 2019-01-01 to 2019-12-31)'
  download_url: https://data.humdata.org/dataset/29ceb0f4-49d9-4c7f-9841-aa4379d119fc/resource/edb86262-66b4-4b11-9421-3c8723021fc5/download/kir_fpanv_m_gdo_20190101_20191221_t.zip
  format: null
  id: resource_edb86262
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: kir_fpanv_m_gdo_20190101_20191221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Kiribati: Copernicus Vegetation Index Anomaly (FAPAR Anomaly) (Data
    from 2018-01-01 to 2018-12-31)'
  download_url: https://data.humdata.org/dataset/29ceb0f4-49d9-4c7f-9841-aa4379d119fc/resource/b3783bdb-30eb-49cf-836a-0ba1cfc3d5b0/download/kir_fpanv_m_gdo_20180101_20181221_t.zip
  format: null
  id: resource_b3783bdb
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: kir_fpanv_m_gdo_20180101_20181221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Kiribati: Copernicus Vegetation Index Anomaly (FAPAR Anomaly) (Data
    from 2017-01-01 to 2017-12-31)'
  download_url: https://data.humdata.org/dataset/29ceb0f4-49d9-4c7f-9841-aa4379d119fc/resource/deed6984-10d1-4e3b-92a0-2755539e4f38/download/kir_fpanv_m_gdo_20170101_20171221_t.zip
  format: null
  id: resource_deed6984
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: kir_fpanv_m_gdo_20170101_20171221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Kiribati: Copernicus Vegetation Index Anomaly (FAPAR Anomaly) (Data
    from 2016-01-01 to 2016-12-31)'
  download_url: https://data.humdata.org/dataset/29ceb0f4-49d9-4c7f-9841-aa4379d119fc/resource/cb0f2c25-8267-447d-bf5e-afc262eea14b/download/kir_fpanv_m_gdo_20160101_20161221_t.zip
  format: null
  id: resource_cb0f2c25
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: kir_fpanv_m_gdo_20160101_20161221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Kiribati: Copernicus Vegetation Index Anomaly (FAPAR Anomaly) (Data
    from 2015-01-01 to 2015-12-31)'
  download_url: https://data.humdata.org/dataset/29ceb0f4-49d9-4c7f-9841-aa4379d119fc/resource/2f6f7a9a-2fdc-4cc6-b089-242be3df21ba/download/kir_fpanv_m_gdo_20150101_20151221_t.zip
  format: null
  id: resource_2f6f7a9a
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: kir_fpanv_m_gdo_20150101_20151221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Kiribati: Copernicus Vegetation Index Anomaly (FAPAR Anomaly) (Data
    from 2014-01-01 to 2014-12-31)'
  download_url: https://data.humdata.org/dataset/29ceb0f4-49d9-4c7f-9841-aa4379d119fc/resource/b2376502-2296-4b98-aa44-f66f7be9f6c8/download/kir_fpanv_m_gdo_20140101_20141221_t.zip
  format: null
  id: resource_b2376502
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: kir_fpanv_m_gdo_20140101_20141221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Kiribati: Copernicus Vegetation Index Anomaly (FAPAR Anomaly) (Data
    from 2013-01-01 to 2013-12-31)'
  download_url: https://data.humdata.org/dataset/29ceb0f4-49d9-4c7f-9841-aa4379d119fc/resource/bc44ef0a-7be1-45f3-9aaf-3b0d5c665c48/download/kir_fpanv_m_gdo_20130101_20131221_t.zip
  format: null
  id: resource_bc44ef0a
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: kir_fpanv_m_gdo_20130101_20131221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Kiribati: Copernicus Vegetation Index Anomaly (FAPAR Anomaly) (Data
    from 2012-01-21 to 2012-12-31)'
  download_url: https://data.humdata.org/dataset/29ceb0f4-49d9-4c7f-9841-aa4379d119fc/resource/570b3e64-f7a7-4813-9056-ad1fb60bcfc1/download/kir_fpanv_m_gdo_20120121_20121221_t.zip
  format: null
  id: resource_570b3e64
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: kir_fpanv_m_gdo_20120121_20121221_t.zip
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-kir_copernicus_vegetationindexanomalyfap_2012
spatial:
  bbox: null
  centroid: null
  countries:
  - KIR
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2026-01-10'
  start: '2012-01-21'
temporal_resolution: null
title: 'Kiribati: Copernicus Vegetation Index Anomaly (FAPAR Anomaly)'
version: null
vulnerability: null
---
