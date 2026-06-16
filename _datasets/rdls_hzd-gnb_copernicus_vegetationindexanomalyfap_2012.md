---
attributions:
- entity:
    affiliation: null
    email: null
    name: Copernicus / European Commission Joint Research Centre (JRC)
    url: https://data.humdata.org/dataset/gnb-anomalies-fapar-viirs
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Copernicus
  url: https://data.humdata.org/dataset/gnb-anomalies-fapar-viirs
creator:
  affiliation: null
  email: null
  name: Copernicus
  url: https://data.humdata.org/dataset/gnb-anomalies-fapar-viirs
dataset_id: rdls_hzd-gnb_copernicus_vegetationindexanomalyfap_2012
description: 'Fraction of Absorbed Photosynthetically Active Radiation (FAPAR) is
  a biophysical dimensionless quantity (its values range from 0/no absorption to 1/total
  absorption) used to assess the greenness and health of vegetation. FAPAR anomalies
  can be used as an indicator to detect and monitor the impacts of agricultural drought
  on the growth and productivity of vegetation. The data is presented in 10-day time
  composite of the Visible Infrared Imaging Radiometer Suite (VIIRS).. [Source: This
  metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/gnb-anomalies-fapar-viirs]'
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
  description: VIIRS satellite observations of photosynthetically active radiation
    absorption are processed into 10-day temporal composites. FAPAR anomalies are
    calculated at each grid cell as the deviation from a long-term mean baseline (2012
    to last complete year), generating raster datasets that serve as an empirical
    indicator of agricultural drought stress on vegetation.
  sources:
  - id: source_1
    license: null
    name: Copernicus / European Commission Joint Research Centre (JRC)
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/gnb-anomalies-fapar-viirs
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
  description: 'Guinea-Bissau: Copernicus Vegetation Index Anomaly (FAPAR Anomaly)
    (Data from 2026-01-01 to 2026-01-10)'
  download_url: https://data.humdata.org/dataset/31edccfa-d524-4a23-bb75-e1428b7e2ed4/resource/9cfab139-8336-4e2b-808c-427e429720a1/download/gnb_fpanv_m_gdo_20260101_20260101_t.zip
  format: null
  id: resource_9cfab139
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gnb_fpanv_m_gdo_20260101_20260101_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Guinea-Bissau: Copernicus Vegetation Index Anomaly (FAPAR Anomaly)
    (Data from 2025-01-01 to 2025-12-31)'
  download_url: https://data.humdata.org/dataset/31edccfa-d524-4a23-bb75-e1428b7e2ed4/resource/041a729c-5ff1-497f-bf67-87d3c0d7eac2/download/gnb_fpanv_m_gdo_20250101_20251221_t.zip
  format: null
  id: resource_041a729c
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gnb_fpanv_m_gdo_20250101_20251221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Guinea-Bissau: Copernicus Vegetation Index Anomaly (FAPAR Anomaly)
    (Data from 2024-01-01 to 2024-12-31)'
  download_url: https://data.humdata.org/dataset/31edccfa-d524-4a23-bb75-e1428b7e2ed4/resource/c59ddf05-48bd-4631-b11e-8dc0f58f2ccc/download/gnb_fpanv_m_gdo_20240101_20241221_t.zip
  format: null
  id: resource_c59ddf05
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gnb_fpanv_m_gdo_20240101_20241221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Guinea-Bissau: Copernicus Vegetation Index Anomaly (FAPAR Anomaly)
    (Data from 2023-01-01 to 2023-12-31)'
  download_url: https://data.humdata.org/dataset/31edccfa-d524-4a23-bb75-e1428b7e2ed4/resource/b702c130-3032-45d7-a6ea-7c3d4a5b8de4/download/gnb_fpanv_m_gdo_20230101_20231221_t.zip
  format: null
  id: resource_b702c130
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gnb_fpanv_m_gdo_20230101_20231221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Guinea-Bissau: Copernicus Vegetation Index Anomaly (FAPAR Anomaly)
    (Data from 2022-01-01 to 2022-12-31)'
  download_url: https://data.humdata.org/dataset/31edccfa-d524-4a23-bb75-e1428b7e2ed4/resource/8a696bd5-5577-4107-81a5-f2ea13f50c94/download/gnb_fpanv_m_gdo_20220101_20221221_t.zip
  format: null
  id: resource_8a696bd5
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gnb_fpanv_m_gdo_20220101_20221221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Guinea-Bissau: Copernicus Vegetation Index Anomaly (FAPAR Anomaly)
    (Data from 2021-01-01 to 2021-12-31)'
  download_url: https://data.humdata.org/dataset/31edccfa-d524-4a23-bb75-e1428b7e2ed4/resource/8385b028-5541-4767-9964-da8975713a66/download/gnb_fpanv_m_gdo_20210101_20211221_t.zip
  format: null
  id: resource_8385b028
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gnb_fpanv_m_gdo_20210101_20211221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Guinea-Bissau: Copernicus Vegetation Index Anomaly (FAPAR Anomaly)
    (Data from 2020-01-01 to 2020-12-31)'
  download_url: https://data.humdata.org/dataset/31edccfa-d524-4a23-bb75-e1428b7e2ed4/resource/21516dbf-4515-4ea4-8008-1d51f91c4f75/download/gnb_fpanv_m_gdo_20200101_20201221_t.zip
  format: null
  id: resource_21516dbf
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gnb_fpanv_m_gdo_20200101_20201221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Guinea-Bissau: Copernicus Vegetation Index Anomaly (FAPAR Anomaly)
    (Data from 2019-01-01 to 2019-12-31)'
  download_url: https://data.humdata.org/dataset/31edccfa-d524-4a23-bb75-e1428b7e2ed4/resource/5bf34447-3187-4cce-838f-279a58c1a133/download/gnb_fpanv_m_gdo_20190101_20191221_t.zip
  format: null
  id: resource_5bf34447
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gnb_fpanv_m_gdo_20190101_20191221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Guinea-Bissau: Copernicus Vegetation Index Anomaly (FAPAR Anomaly)
    (Data from 2018-01-01 to 2018-12-31)'
  download_url: https://data.humdata.org/dataset/31edccfa-d524-4a23-bb75-e1428b7e2ed4/resource/e7a37f6c-b4c8-4541-92c9-eccd20643b4c/download/gnb_fpanv_m_gdo_20180101_20181221_t.zip
  format: null
  id: resource_e7a37f6c
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gnb_fpanv_m_gdo_20180101_20181221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Guinea-Bissau: Copernicus Vegetation Index Anomaly (FAPAR Anomaly)
    (Data from 2017-01-01 to 2017-12-31)'
  download_url: https://data.humdata.org/dataset/31edccfa-d524-4a23-bb75-e1428b7e2ed4/resource/37938561-44df-4bd6-927d-5d905ac300ad/download/gnb_fpanv_m_gdo_20170101_20171221_t.zip
  format: null
  id: resource_37938561
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gnb_fpanv_m_gdo_20170101_20171221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Guinea-Bissau: Copernicus Vegetation Index Anomaly (FAPAR Anomaly)
    (Data from 2016-01-01 to 2016-12-31)'
  download_url: https://data.humdata.org/dataset/31edccfa-d524-4a23-bb75-e1428b7e2ed4/resource/68e07877-b03b-49a5-8f89-6abea922229c/download/gnb_fpanv_m_gdo_20160101_20161221_t.zip
  format: null
  id: resource_68e07877
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gnb_fpanv_m_gdo_20160101_20161221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Guinea-Bissau: Copernicus Vegetation Index Anomaly (FAPAR Anomaly)
    (Data from 2015-01-01 to 2015-12-31)'
  download_url: https://data.humdata.org/dataset/31edccfa-d524-4a23-bb75-e1428b7e2ed4/resource/379dfd3c-bd4d-4059-9308-e9b724346fb9/download/gnb_fpanv_m_gdo_20150101_20151221_t.zip
  format: null
  id: resource_379dfd3c
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gnb_fpanv_m_gdo_20150101_20151221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Guinea-Bissau: Copernicus Vegetation Index Anomaly (FAPAR Anomaly)
    (Data from 2014-01-01 to 2014-12-31)'
  download_url: https://data.humdata.org/dataset/31edccfa-d524-4a23-bb75-e1428b7e2ed4/resource/e9bf17b7-676b-4a0a-9cda-afcfd9a71175/download/gnb_fpanv_m_gdo_20140101_20141221_t.zip
  format: null
  id: resource_e9bf17b7
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gnb_fpanv_m_gdo_20140101_20141221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Guinea-Bissau: Copernicus Vegetation Index Anomaly (FAPAR Anomaly)
    (Data from 2013-01-01 to 2013-12-31)'
  download_url: https://data.humdata.org/dataset/31edccfa-d524-4a23-bb75-e1428b7e2ed4/resource/2c9dd146-88f9-4600-bd82-d304264b82dc/download/gnb_fpanv_m_gdo_20130101_20131221_t.zip
  format: null
  id: resource_2c9dd146
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gnb_fpanv_m_gdo_20130101_20131221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Guinea-Bissau: Copernicus Vegetation Index Anomaly (FAPAR Anomaly)
    (Data from 2012-01-21 to 2012-12-31)'
  download_url: https://data.humdata.org/dataset/31edccfa-d524-4a23-bb75-e1428b7e2ed4/resource/a0108bd7-1551-49d2-8324-19991156c9b0/download/gnb_fpanv_m_gdo_20120121_20121221_t.zip
  format: null
  id: resource_a0108bd7
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gnb_fpanv_m_gdo_20120121_20121221_t.zip
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-gnb_copernicus_vegetationindexanomalyfap_2012
spatial:
  bbox: null
  centroid: null
  countries:
  - GNB
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2026-01-10'
  start: '2012-01-21'
temporal_resolution: null
title: 'Guinea-Bissau: Copernicus Vegetation Index Anomaly (FAPAR Anomaly)'
version: null
vulnerability: null
---
