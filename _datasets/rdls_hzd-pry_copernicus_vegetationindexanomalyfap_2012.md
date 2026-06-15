---
attributions:
- entity:
    affiliation: null
    email: null
    name: European Commission, Joint Research Centre (JRC)
    url: https://data.humdata.org/dataset/pry-anomalies-fapar-viirs
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Copernicus
  url: https://data.humdata.org/dataset/pry-anomalies-fapar-viirs
creator:
  affiliation: null
  email: null
  name: Copernicus
  url: https://data.humdata.org/dataset/pry-anomalies-fapar-viirs
dataset_id: rdls_hzd-pry_copernicus_vegetationindexanomalyfap_2012
description: 'Fraction of Absorbed Photosynthetically Active Radiation (FAPAR) is
  a biophysical dimensionless quantity (its values range from 0/no absorption to 1/total
  absorption) used to assess the greenness and health of vegetation. FAPAR anomalies
  can be used as an indicator to detect and monitor the impacts of agricultural drought
  on the growth and productivity of vegetation. The data is presented in 10-day time
  composite of the Visible Infrared Imaging Radiometer Suite (VIIRS).. [Source: This
  metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/pry-anomalies-fapar-viirs]'
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
  description: FAPAR values from VIIRS satellite observations are composited at 10-day
    intervals. Anomalies are calculated by computing the deviation of each grid cell's
    FAPAR value from its long-term mean baseline (2012 to the last available full
    year), producing raster datasets that serve as an empirical indicator of agricultural
    drought stress on vegetation.
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
- href: https://data.humdata.org/dataset/pry-anomalies-fapar-viirs
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
  description: 'Paraguay: Copernicus Vegetation Index Anomaly (FAPAR Anomaly) (Data
    from 2026-01-01 to 2026-01-10)'
  download_url: https://data.humdata.org/dataset/863b9891-6eb5-43b1-97aa-17c834118605/resource/bf656886-2220-42de-b70b-fc8e5b81b6d9/download/pry_fpanv_m_gdo_20260101_20260101_t.zip
  format: null
  id: resource_bf656886
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: pry_fpanv_m_gdo_20260101_20260101_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Paraguay: Copernicus Vegetation Index Anomaly (FAPAR Anomaly) (Data
    from 2025-01-01 to 2025-12-31)'
  download_url: https://data.humdata.org/dataset/863b9891-6eb5-43b1-97aa-17c834118605/resource/9f45259a-11a5-4c0d-bd0f-fa6fe63a09dc/download/pry_fpanv_m_gdo_20250101_20251221_t.zip
  format: null
  id: resource_9f45259a
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: pry_fpanv_m_gdo_20250101_20251221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Paraguay: Copernicus Vegetation Index Anomaly (FAPAR Anomaly) (Data
    from 2024-01-01 to 2024-12-31)'
  download_url: https://data.humdata.org/dataset/863b9891-6eb5-43b1-97aa-17c834118605/resource/a779ccd7-e4ef-44a7-a399-b20e3ab297ef/download/pry_fpanv_m_gdo_20240101_20241221_t.zip
  format: null
  id: resource_a779ccd7
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: pry_fpanv_m_gdo_20240101_20241221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Paraguay: Copernicus Vegetation Index Anomaly (FAPAR Anomaly) (Data
    from 2023-01-01 to 2023-12-31)'
  download_url: https://data.humdata.org/dataset/863b9891-6eb5-43b1-97aa-17c834118605/resource/aba82b5a-2343-4b7d-bad3-7d983d105fd7/download/pry_fpanv_m_gdo_20230101_20231221_t.zip
  format: null
  id: resource_aba82b5a
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: pry_fpanv_m_gdo_20230101_20231221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Paraguay: Copernicus Vegetation Index Anomaly (FAPAR Anomaly) (Data
    from 2022-01-01 to 2022-12-31)'
  download_url: https://data.humdata.org/dataset/863b9891-6eb5-43b1-97aa-17c834118605/resource/07c9ab11-9ab0-48d8-99ef-81b9d7d9bbe4/download/pry_fpanv_m_gdo_20220101_20221221_t.zip
  format: null
  id: resource_07c9ab11
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: pry_fpanv_m_gdo_20220101_20221221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Paraguay: Copernicus Vegetation Index Anomaly (FAPAR Anomaly) (Data
    from 2021-01-01 to 2021-12-31)'
  download_url: https://data.humdata.org/dataset/863b9891-6eb5-43b1-97aa-17c834118605/resource/f78154eb-d261-4901-aa9a-0d9320af232d/download/pry_fpanv_m_gdo_20210101_20211221_t.zip
  format: null
  id: resource_f78154eb
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: pry_fpanv_m_gdo_20210101_20211221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Paraguay: Copernicus Vegetation Index Anomaly (FAPAR Anomaly) (Data
    from 2020-01-01 to 2020-12-31)'
  download_url: https://data.humdata.org/dataset/863b9891-6eb5-43b1-97aa-17c834118605/resource/fefe0ba8-383f-457a-bd4f-6a8c03546618/download/pry_fpanv_m_gdo_20200101_20201221_t.zip
  format: null
  id: resource_fefe0ba8
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: pry_fpanv_m_gdo_20200101_20201221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Paraguay: Copernicus Vegetation Index Anomaly (FAPAR Anomaly) (Data
    from 2019-01-01 to 2019-12-31)'
  download_url: https://data.humdata.org/dataset/863b9891-6eb5-43b1-97aa-17c834118605/resource/5aab4059-267a-4006-b6b3-85de7be3b19b/download/pry_fpanv_m_gdo_20190101_20191221_t.zip
  format: null
  id: resource_5aab4059
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: pry_fpanv_m_gdo_20190101_20191221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Paraguay: Copernicus Vegetation Index Anomaly (FAPAR Anomaly) (Data
    from 2018-01-01 to 2018-12-31)'
  download_url: https://data.humdata.org/dataset/863b9891-6eb5-43b1-97aa-17c834118605/resource/4236ddff-4def-409d-9672-ba4cfea7147b/download/pry_fpanv_m_gdo_20180101_20181221_t.zip
  format: null
  id: resource_4236ddff
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: pry_fpanv_m_gdo_20180101_20181221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Paraguay: Copernicus Vegetation Index Anomaly (FAPAR Anomaly) (Data
    from 2017-01-01 to 2017-12-31)'
  download_url: https://data.humdata.org/dataset/863b9891-6eb5-43b1-97aa-17c834118605/resource/d2b1453d-b976-4700-8798-fec09093dfa1/download/pry_fpanv_m_gdo_20170101_20171221_t.zip
  format: null
  id: resource_d2b1453d
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: pry_fpanv_m_gdo_20170101_20171221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Paraguay: Copernicus Vegetation Index Anomaly (FAPAR Anomaly) (Data
    from 2016-01-01 to 2016-12-31)'
  download_url: https://data.humdata.org/dataset/863b9891-6eb5-43b1-97aa-17c834118605/resource/30660bb9-54cf-4bef-89c3-5832d3a2ba47/download/pry_fpanv_m_gdo_20160101_20161221_t.zip
  format: null
  id: resource_30660bb9
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: pry_fpanv_m_gdo_20160101_20161221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Paraguay: Copernicus Vegetation Index Anomaly (FAPAR Anomaly) (Data
    from 2015-01-01 to 2015-12-31)'
  download_url: https://data.humdata.org/dataset/863b9891-6eb5-43b1-97aa-17c834118605/resource/9fc193f5-ebbf-47c1-ac32-334d2832df05/download/pry_fpanv_m_gdo_20150101_20151221_t.zip
  format: null
  id: resource_9fc193f5
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: pry_fpanv_m_gdo_20150101_20151221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Paraguay: Copernicus Vegetation Index Anomaly (FAPAR Anomaly) (Data
    from 2014-01-01 to 2014-12-31)'
  download_url: https://data.humdata.org/dataset/863b9891-6eb5-43b1-97aa-17c834118605/resource/7f81bc54-c29e-4a59-a9b5-d7800161d78c/download/pry_fpanv_m_gdo_20140101_20141221_t.zip
  format: null
  id: resource_7f81bc54
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: pry_fpanv_m_gdo_20140101_20141221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Paraguay: Copernicus Vegetation Index Anomaly (FAPAR Anomaly) (Data
    from 2013-01-01 to 2013-12-31)'
  download_url: https://data.humdata.org/dataset/863b9891-6eb5-43b1-97aa-17c834118605/resource/4baf0f64-3044-4394-809e-6d3a90e2b894/download/pry_fpanv_m_gdo_20130101_20131221_t.zip
  format: null
  id: resource_4baf0f64
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: pry_fpanv_m_gdo_20130101_20131221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Paraguay: Copernicus Vegetation Index Anomaly (FAPAR Anomaly) (Data
    from 2012-01-21 to 2012-12-31)'
  download_url: https://data.humdata.org/dataset/863b9891-6eb5-43b1-97aa-17c834118605/resource/e96bf4e3-ea25-4966-b4f8-5b04b28fd5df/download/pry_fpanv_m_gdo_20120121_20121221_t.zip
  format: null
  id: resource_e96bf4e3
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: pry_fpanv_m_gdo_20120121_20121221_t.zip
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-pry_copernicus_vegetationindexanomalyfap_2012
spatial:
  bbox: null
  centroid: null
  countries:
  - PRY
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2026-01-10'
  start: '2012-01-21'
temporal_resolution: null
title: 'Paraguay: Copernicus Vegetation Index Anomaly (FAPAR Anomaly)'
version: null
vulnerability: null
---
