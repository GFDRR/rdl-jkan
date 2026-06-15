---
attributions:
- entity:
    affiliation: null
    email: null
    name: Copernicus Emergency Management Service (CEMS)
    url: https://data.humdata.org/dataset/irq-anomalies-fapar-viirs
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Copernicus
  url: https://data.humdata.org/dataset/irq-anomalies-fapar-viirs
creator:
  affiliation: null
  email: null
  name: Copernicus
  url: https://data.humdata.org/dataset/irq-anomalies-fapar-viirs
dataset_id: rdls_hzd-irq_copernicus_vegetationindexanomalyfap_2012
description: 'Fraction of Absorbed Photosynthetically Active Radiation (FAPAR) is
  a biophysical dimensionless quantity (its values range from 0/no absorption to 1/total
  absorption) used to assess the greenness and health of vegetation. FAPAR anomalies
  can be used as an indicator to detect and monitor the impacts of agricultural drought
  on the growth and productivity of vegetation. The data is presented in 10-day time
  composite of the Visible Infrared Imaging Radiometer Suite (VIIRS).. [Source: This
  metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/irq-anomalies-fapar-viirs]'
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
    intervals and processed into raster composites. FAPAR anomalies are calculated
    at each grid cell as the deviation from a long-term mean baseline (2012 to the
    last available full year), enabling detection and monitoring of agricultural drought
    impacts on vegetation growth and productivity across Iraq.
  sources:
  - id: source_1
    license: null
    name: Copernicus Emergency Management Service (CEMS)
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/irq-anomalies-fapar-viirs
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
  description: 'Iraq: Copernicus Vegetation Index Anomaly (FAPAR Anomaly) (Data from
    2026-01-01 to 2026-01-10)'
  download_url: https://data.humdata.org/dataset/eccef827-e4dd-458f-ae50-7b2e9e10be38/resource/2a13e65e-a184-444e-92b0-0a81a50d52f3/download/irq_fpanv_m_gdo_20260101_20260101_t.zip
  format: null
  id: resource_2a13e65e
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: irq_fpanv_m_gdo_20260101_20260101_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Iraq: Copernicus Vegetation Index Anomaly (FAPAR Anomaly) (Data from
    2025-01-01 to 2025-12-31)'
  download_url: https://data.humdata.org/dataset/eccef827-e4dd-458f-ae50-7b2e9e10be38/resource/4a107053-8ce5-43c5-8acb-6a5f92baa81f/download/irq_fpanv_m_gdo_20250101_20251221_t.zip
  format: null
  id: resource_4a107053
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: irq_fpanv_m_gdo_20250101_20251221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Iraq: Copernicus Vegetation Index Anomaly (FAPAR Anomaly) (Data from
    2024-01-01 to 2024-12-31)'
  download_url: https://data.humdata.org/dataset/eccef827-e4dd-458f-ae50-7b2e9e10be38/resource/05f6028b-cb5d-4050-bf12-3196afd23997/download/irq_fpanv_m_gdo_20240101_20241221_t.zip
  format: null
  id: resource_05f6028b
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: irq_fpanv_m_gdo_20240101_20241221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Iraq: Copernicus Vegetation Index Anomaly (FAPAR Anomaly) (Data from
    2023-01-01 to 2023-12-31)'
  download_url: https://data.humdata.org/dataset/eccef827-e4dd-458f-ae50-7b2e9e10be38/resource/ebec8a0f-a45d-40f7-a2d1-641b2a6409fc/download/irq_fpanv_m_gdo_20230101_20231221_t.zip
  format: null
  id: resource_ebec8a0f
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: irq_fpanv_m_gdo_20230101_20231221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Iraq: Copernicus Vegetation Index Anomaly (FAPAR Anomaly) (Data from
    2022-01-01 to 2022-12-31)'
  download_url: https://data.humdata.org/dataset/eccef827-e4dd-458f-ae50-7b2e9e10be38/resource/3f851a4c-776e-4e28-ae8f-40f5ec48c166/download/irq_fpanv_m_gdo_20220101_20221221_t.zip
  format: null
  id: resource_3f851a4c
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: irq_fpanv_m_gdo_20220101_20221221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Iraq: Copernicus Vegetation Index Anomaly (FAPAR Anomaly) (Data from
    2021-01-01 to 2021-12-31)'
  download_url: https://data.humdata.org/dataset/eccef827-e4dd-458f-ae50-7b2e9e10be38/resource/43f37da4-dca3-4142-bc02-9829766c3879/download/irq_fpanv_m_gdo_20210101_20211221_t.zip
  format: null
  id: resource_43f37da4
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: irq_fpanv_m_gdo_20210101_20211221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Iraq: Copernicus Vegetation Index Anomaly (FAPAR Anomaly) (Data from
    2020-01-01 to 2020-12-31)'
  download_url: https://data.humdata.org/dataset/eccef827-e4dd-458f-ae50-7b2e9e10be38/resource/a58b6c82-7666-4561-bd66-8f72ef3dda6d/download/irq_fpanv_m_gdo_20200101_20201221_t.zip
  format: null
  id: resource_a58b6c82
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: irq_fpanv_m_gdo_20200101_20201221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Iraq: Copernicus Vegetation Index Anomaly (FAPAR Anomaly) (Data from
    2019-01-01 to 2019-12-31)'
  download_url: https://data.humdata.org/dataset/eccef827-e4dd-458f-ae50-7b2e9e10be38/resource/4a921b96-faca-4add-9bfe-1b4ed04260e1/download/irq_fpanv_m_gdo_20190101_20191221_t.zip
  format: null
  id: resource_4a921b96
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: irq_fpanv_m_gdo_20190101_20191221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Iraq: Copernicus Vegetation Index Anomaly (FAPAR Anomaly) (Data from
    2018-01-01 to 2018-12-31)'
  download_url: https://data.humdata.org/dataset/eccef827-e4dd-458f-ae50-7b2e9e10be38/resource/cc8c3281-b5cb-452c-83ef-db689504e2fb/download/irq_fpanv_m_gdo_20180101_20181221_t.zip
  format: null
  id: resource_cc8c3281
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: irq_fpanv_m_gdo_20180101_20181221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Iraq: Copernicus Vegetation Index Anomaly (FAPAR Anomaly) (Data from
    2017-01-01 to 2017-12-31)'
  download_url: https://data.humdata.org/dataset/eccef827-e4dd-458f-ae50-7b2e9e10be38/resource/faebc070-7702-475a-af2c-39cd2e51d510/download/irq_fpanv_m_gdo_20170101_20171221_t.zip
  format: null
  id: resource_faebc070
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: irq_fpanv_m_gdo_20170101_20171221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Iraq: Copernicus Vegetation Index Anomaly (FAPAR Anomaly) (Data from
    2016-01-01 to 2016-12-31)'
  download_url: https://data.humdata.org/dataset/eccef827-e4dd-458f-ae50-7b2e9e10be38/resource/d0670a3d-9c22-499f-b354-28772155d3ac/download/irq_fpanv_m_gdo_20160101_20161221_t.zip
  format: null
  id: resource_d0670a3d
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: irq_fpanv_m_gdo_20160101_20161221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Iraq: Copernicus Vegetation Index Anomaly (FAPAR Anomaly) (Data from
    2015-01-01 to 2015-12-31)'
  download_url: https://data.humdata.org/dataset/eccef827-e4dd-458f-ae50-7b2e9e10be38/resource/3bedef54-9fb7-4f43-82a2-6fa94a8ed392/download/irq_fpanv_m_gdo_20150101_20151221_t.zip
  format: null
  id: resource_3bedef54
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: irq_fpanv_m_gdo_20150101_20151221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Iraq: Copernicus Vegetation Index Anomaly (FAPAR Anomaly) (Data from
    2014-01-01 to 2014-12-31)'
  download_url: https://data.humdata.org/dataset/eccef827-e4dd-458f-ae50-7b2e9e10be38/resource/b09e2233-8c58-400c-ba94-e9b8de99ee90/download/irq_fpanv_m_gdo_20140101_20141221_t.zip
  format: null
  id: resource_b09e2233
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: irq_fpanv_m_gdo_20140101_20141221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Iraq: Copernicus Vegetation Index Anomaly (FAPAR Anomaly) (Data from
    2013-01-01 to 2013-12-31)'
  download_url: https://data.humdata.org/dataset/eccef827-e4dd-458f-ae50-7b2e9e10be38/resource/3f55e50d-c65d-4a7c-a31a-4f0330c0ad74/download/irq_fpanv_m_gdo_20130101_20131221_t.zip
  format: null
  id: resource_3f55e50d
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: irq_fpanv_m_gdo_20130101_20131221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Iraq: Copernicus Vegetation Index Anomaly (FAPAR Anomaly) (Data from
    2012-01-21 to 2012-12-31)'
  download_url: https://data.humdata.org/dataset/eccef827-e4dd-458f-ae50-7b2e9e10be38/resource/747bd104-f38e-4cdf-b6c1-6a91c4fe57a8/download/irq_fpanv_m_gdo_20120121_20121221_t.zip
  format: null
  id: resource_747bd104
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: irq_fpanv_m_gdo_20120121_20121221_t.zip
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-irq_copernicus_vegetationindexanomalyfap_2012
spatial:
  bbox: null
  centroid: null
  countries:
  - IRQ
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2026-01-10'
  start: '2012-01-21'
temporal_resolution: null
title: 'Iraq: Copernicus Vegetation Index Anomaly (FAPAR Anomaly)'
version: null
vulnerability: null
---
