---
attributions:
- entity:
    affiliation: null
    email: null
    name: Copernicus / European Commission Joint Research Centre (JRC)
    url: https://data.humdata.org/dataset/fro-anomalies-fapar-viirs
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Copernicus
  url: https://data.humdata.org/dataset/fro-anomalies-fapar-viirs
creator:
  affiliation: null
  email: null
  name: Copernicus
  url: https://data.humdata.org/dataset/fro-anomalies-fapar-viirs
dataset_id: rdls_hzd-fro_copernicus_faroeislandsvegetationind_2012
description: 'Fraction of Absorbed Photosynthetically Active Radiation (FAPAR) is
  a biophysical dimensionless quantity (its values range from 0/no absorption to 1/total
  absorption) used to assess the greenness and health of vegetation. FAPAR anomalies
  can be used as an indicator to detect and monitor the impacts of agricultural drought
  on the growth and productivity of vegetation. The data is presented in 10-day time
  composite of the Visible Infrared Imaging Radiometer Suite (VIIRS).. [Source: This
  metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/fro-anomalies-fapar-viirs]'
details: Variations in the vegetation health and/or cover could be related to stress
  factors not related to droughts (e.g., plant diseases, pests, hail, flooding). To
  determine if changes in FAPAR are linked with a drought event or not, FAPAR data
  should be interpreted jointly with other indicators (as in the EDO Combined Drought
  Indicator).
exposure: []
hazard:
  event_sets:
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
  type: drought
license: CC-BY-4.0
lineage:
  description: FAPAR values derived from VIIRS satellite radiometer observations are
    composited at 10-day intervals. Anomalies are calculated at each grid cell as
    the deviation from a long-term mean baseline (2012 to last complete year), producing
    raster datasets that serve as an empirical indicator of agricultural drought stress
    on vegetation productivity.
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
- href: https://data.humdata.org/dataset/fro-anomalies-fapar-viirs
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
  description: 'Faroe Islands: Copernicus Vegetation Index Anomaly (FAPAR Anomaly)
    (Data from 2026-01-01 to 2026-01-10)'
  download_url: https://data.humdata.org/dataset/ac17827f-2788-4672-8222-4f2b4c01f76f/resource/653698a5-2007-460a-8760-b78e2d51f1e4/download/fro_fpanv_m_gdo_20260101_20260101_t.zip
  format: null
  id: resource_653698a5
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: fro_fpanv_m_gdo_20260101_20260101_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Faroe Islands: Copernicus Vegetation Index Anomaly (FAPAR Anomaly)
    (Data from 2025-01-01 to 2025-12-31)'
  download_url: https://data.humdata.org/dataset/ac17827f-2788-4672-8222-4f2b4c01f76f/resource/c60421c3-44b2-4db5-bf96-7bfa9f798cb1/download/fro_fpanv_m_gdo_20250101_20251221_t.zip
  format: null
  id: resource_c60421c3
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: fro_fpanv_m_gdo_20250101_20251221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Faroe Islands: Copernicus Vegetation Index Anomaly (FAPAR Anomaly)
    (Data from 2024-01-01 to 2024-12-31)'
  download_url: https://data.humdata.org/dataset/ac17827f-2788-4672-8222-4f2b4c01f76f/resource/aba3ea7a-5101-430c-936f-d2d7116c8061/download/fro_fpanv_m_gdo_20240101_20241221_t.zip
  format: null
  id: resource_aba3ea7a
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: fro_fpanv_m_gdo_20240101_20241221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Faroe Islands: Copernicus Vegetation Index Anomaly (FAPAR Anomaly)
    (Data from 2023-01-01 to 2023-12-31)'
  download_url: https://data.humdata.org/dataset/ac17827f-2788-4672-8222-4f2b4c01f76f/resource/7fb868de-41f0-4729-a4fc-531a363e1841/download/fro_fpanv_m_gdo_20230101_20231221_t.zip
  format: null
  id: resource_7fb868de
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: fro_fpanv_m_gdo_20230101_20231221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Faroe Islands: Copernicus Vegetation Index Anomaly (FAPAR Anomaly)
    (Data from 2022-01-01 to 2022-12-31)'
  download_url: https://data.humdata.org/dataset/ac17827f-2788-4672-8222-4f2b4c01f76f/resource/fcd7447b-36d8-4d9a-8e70-41cfb7dc1999/download/fro_fpanv_m_gdo_20220101_20221221_t.zip
  format: null
  id: resource_fcd7447b
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: fro_fpanv_m_gdo_20220101_20221221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Faroe Islands: Copernicus Vegetation Index Anomaly (FAPAR Anomaly)
    (Data from 2021-01-01 to 2021-12-31)'
  download_url: https://data.humdata.org/dataset/ac17827f-2788-4672-8222-4f2b4c01f76f/resource/0809cbcb-540a-4618-8dd5-c7f43d433e6a/download/fro_fpanv_m_gdo_20210101_20211221_t.zip
  format: null
  id: resource_0809cbcb
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: fro_fpanv_m_gdo_20210101_20211221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Faroe Islands: Copernicus Vegetation Index Anomaly (FAPAR Anomaly)
    (Data from 2020-01-01 to 2020-12-31)'
  download_url: https://data.humdata.org/dataset/ac17827f-2788-4672-8222-4f2b4c01f76f/resource/b571767e-e649-4765-891c-ad4b59405a8d/download/fro_fpanv_m_gdo_20200101_20201221_t.zip
  format: null
  id: resource_b571767e
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: fro_fpanv_m_gdo_20200101_20201221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Faroe Islands: Copernicus Vegetation Index Anomaly (FAPAR Anomaly)
    (Data from 2019-01-01 to 2019-12-31)'
  download_url: https://data.humdata.org/dataset/ac17827f-2788-4672-8222-4f2b4c01f76f/resource/997dcbfa-97d7-45d4-91fc-c2b6f32465ec/download/fro_fpanv_m_gdo_20190101_20191221_t.zip
  format: null
  id: resource_997dcbfa
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: fro_fpanv_m_gdo_20190101_20191221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Faroe Islands: Copernicus Vegetation Index Anomaly (FAPAR Anomaly)
    (Data from 2018-01-01 to 2018-12-31)'
  download_url: https://data.humdata.org/dataset/ac17827f-2788-4672-8222-4f2b4c01f76f/resource/88d192dd-7e42-4ed7-974e-2179939bb4f8/download/fro_fpanv_m_gdo_20180101_20181221_t.zip
  format: null
  id: resource_88d192dd
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: fro_fpanv_m_gdo_20180101_20181221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Faroe Islands: Copernicus Vegetation Index Anomaly (FAPAR Anomaly)
    (Data from 2017-01-01 to 2017-12-31)'
  download_url: https://data.humdata.org/dataset/ac17827f-2788-4672-8222-4f2b4c01f76f/resource/78fdf1e0-eeac-41b6-8551-25c735b70bde/download/fro_fpanv_m_gdo_20170101_20171221_t.zip
  format: null
  id: resource_78fdf1e0
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: fro_fpanv_m_gdo_20170101_20171221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Faroe Islands: Copernicus Vegetation Index Anomaly (FAPAR Anomaly)
    (Data from 2016-01-01 to 2016-12-31)'
  download_url: https://data.humdata.org/dataset/ac17827f-2788-4672-8222-4f2b4c01f76f/resource/3e8d5dfe-f5f3-4db7-85c2-6cd92bde0b3b/download/fro_fpanv_m_gdo_20160101_20161221_t.zip
  format: null
  id: resource_3e8d5dfe
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: fro_fpanv_m_gdo_20160101_20161221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Faroe Islands: Copernicus Vegetation Index Anomaly (FAPAR Anomaly)
    (Data from 2015-01-01 to 2015-12-31)'
  download_url: https://data.humdata.org/dataset/ac17827f-2788-4672-8222-4f2b4c01f76f/resource/6fe89b66-6936-417b-b941-454228bd2f01/download/fro_fpanv_m_gdo_20150101_20151221_t.zip
  format: null
  id: resource_6fe89b66
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: fro_fpanv_m_gdo_20150101_20151221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Faroe Islands: Copernicus Vegetation Index Anomaly (FAPAR Anomaly)
    (Data from 2014-01-01 to 2014-12-31)'
  download_url: https://data.humdata.org/dataset/ac17827f-2788-4672-8222-4f2b4c01f76f/resource/cd22368d-7730-49b5-8585-363a2b1953a7/download/fro_fpanv_m_gdo_20140101_20141221_t.zip
  format: null
  id: resource_cd22368d
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: fro_fpanv_m_gdo_20140101_20141221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Faroe Islands: Copernicus Vegetation Index Anomaly (FAPAR Anomaly)
    (Data from 2013-01-01 to 2013-12-31)'
  download_url: https://data.humdata.org/dataset/ac17827f-2788-4672-8222-4f2b4c01f76f/resource/7cd366c9-0edf-44b6-9093-0ef5d721fa9c/download/fro_fpanv_m_gdo_20130101_20131221_t.zip
  format: null
  id: resource_7cd366c9
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: fro_fpanv_m_gdo_20130101_20131221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Faroe Islands: Copernicus Vegetation Index Anomaly (FAPAR Anomaly)
    (Data from 2012-01-21 to 2012-12-31)'
  download_url: https://data.humdata.org/dataset/ac17827f-2788-4672-8222-4f2b4c01f76f/resource/a5c9b14b-e761-4176-abf7-4aef914102dd/download/fro_fpanv_m_gdo_20120121_20121221_t.zip
  format: null
  id: resource_a5c9b14b
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: fro_fpanv_m_gdo_20120121_20121221_t.zip
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-fro_copernicus_faroeislandsvegetationind_2012
spatial:
  bbox: null
  centroid: null
  countries:
  - FRO
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2026-01-10'
  start: '2012-01-21'
temporal_resolution: null
title: 'Faroe Islands: Copernicus Vegetation Index Anomaly (FAPAR Anomaly)'
version: null
vulnerability: null
---
