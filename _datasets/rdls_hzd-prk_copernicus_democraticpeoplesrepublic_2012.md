---
attributions:
- entity:
    affiliation: null
    email: null
    name: European Commission, Joint Research Centre (JRC)
    url: https://data.humdata.org/dataset/prk-anomalies-fapar-viirs
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Copernicus
  url: https://data.humdata.org/dataset/prk-anomalies-fapar-viirs
creator:
  affiliation: null
  email: null
  name: Copernicus
  url: https://data.humdata.org/dataset/prk-anomalies-fapar-viirs
dataset_id: rdls_hzd-prk_copernicus_democraticpeoplesrepublic_2012
description: 'Fraction of Absorbed Photosynthetically Active Radiation (FAPAR) is
  a biophysical dimensionless quantity (its values range from 0/no absorption to 1/total
  absorption) used to assess the greenness and health of vegetation. FAPAR anomalies
  can be used as an indicator to detect and monitor the impacts of agricultural drought
  on the growth and productivity of vegetation. The data is presented in 10-day time
  composite of the Visible Infrared Imaging Radiometer Suite (VIIRS).. [Source: This
  metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/prk-anomalies-fapar-viirs]'
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
license: CC-BY-4.0
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
- href: https://data.humdata.org/dataset/prk-anomalies-fapar-viirs
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
  description: 'Democratic People''s Republic of Korea: Copernicus Vegetation Index
    Anomaly (FAPAR Anomaly) (Data from 2026-01-01 to 2026-01-10)'
  download_url: https://data.humdata.org/dataset/1e3e1610-5578-40bd-b51b-88dc029265ff/resource/0396adaf-dcd3-4325-94a0-c1d6126b67bf/download/prk_fpanv_m_gdo_20260101_20260101_t.zip
  format: null
  id: resource_0396adaf
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: prk_fpanv_m_gdo_20260101_20260101_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Democratic People''s Republic of Korea: Copernicus Vegetation Index
    Anomaly (FAPAR Anomaly) (Data from 2025-01-01 to 2025-12-31)'
  download_url: https://data.humdata.org/dataset/1e3e1610-5578-40bd-b51b-88dc029265ff/resource/13355e63-eefb-4e81-ae86-22c91fc2729c/download/prk_fpanv_m_gdo_20250101_20251221_t.zip
  format: null
  id: resource_13355e63
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: prk_fpanv_m_gdo_20250101_20251221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Democratic People''s Republic of Korea: Copernicus Vegetation Index
    Anomaly (FAPAR Anomaly) (Data from 2024-01-01 to 2024-12-31)'
  download_url: https://data.humdata.org/dataset/1e3e1610-5578-40bd-b51b-88dc029265ff/resource/41f4fe69-e04f-40e8-af84-fed7871be4ab/download/prk_fpanv_m_gdo_20240101_20241221_t.zip
  format: null
  id: resource_41f4fe69
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: prk_fpanv_m_gdo_20240101_20241221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Democratic People''s Republic of Korea: Copernicus Vegetation Index
    Anomaly (FAPAR Anomaly) (Data from 2023-01-01 to 2023-12-31)'
  download_url: https://data.humdata.org/dataset/1e3e1610-5578-40bd-b51b-88dc029265ff/resource/c4890fcd-385a-4565-8a3a-dbfc232a6337/download/prk_fpanv_m_gdo_20230101_20231221_t.zip
  format: null
  id: resource_c4890fcd
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: prk_fpanv_m_gdo_20230101_20231221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Democratic People''s Republic of Korea: Copernicus Vegetation Index
    Anomaly (FAPAR Anomaly) (Data from 2022-01-01 to 2022-12-31)'
  download_url: https://data.humdata.org/dataset/1e3e1610-5578-40bd-b51b-88dc029265ff/resource/52d1bdff-8ef6-4666-99c5-3fb8166505ef/download/prk_fpanv_m_gdo_20220101_20221221_t.zip
  format: null
  id: resource_52d1bdff
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: prk_fpanv_m_gdo_20220101_20221221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Democratic People''s Republic of Korea: Copernicus Vegetation Index
    Anomaly (FAPAR Anomaly) (Data from 2021-01-01 to 2021-12-31)'
  download_url: https://data.humdata.org/dataset/1e3e1610-5578-40bd-b51b-88dc029265ff/resource/aff6ea97-18e4-4e6b-9f44-ad7603307bdd/download/prk_fpanv_m_gdo_20210101_20211221_t.zip
  format: null
  id: resource_aff6ea97
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: prk_fpanv_m_gdo_20210101_20211221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Democratic People''s Republic of Korea: Copernicus Vegetation Index
    Anomaly (FAPAR Anomaly) (Data from 2020-01-01 to 2020-12-31)'
  download_url: https://data.humdata.org/dataset/1e3e1610-5578-40bd-b51b-88dc029265ff/resource/2ba266cb-39e2-4897-ad16-5be9c23a9453/download/prk_fpanv_m_gdo_20200101_20201221_t.zip
  format: null
  id: resource_2ba266cb
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: prk_fpanv_m_gdo_20200101_20201221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Democratic People''s Republic of Korea: Copernicus Vegetation Index
    Anomaly (FAPAR Anomaly) (Data from 2019-01-01 to 2019-12-31)'
  download_url: https://data.humdata.org/dataset/1e3e1610-5578-40bd-b51b-88dc029265ff/resource/be6aae7c-a178-44e6-946c-54bde851ff28/download/prk_fpanv_m_gdo_20190101_20191221_t.zip
  format: null
  id: resource_be6aae7c
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: prk_fpanv_m_gdo_20190101_20191221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Democratic People''s Republic of Korea: Copernicus Vegetation Index
    Anomaly (FAPAR Anomaly) (Data from 2018-01-01 to 2018-12-31)'
  download_url: https://data.humdata.org/dataset/1e3e1610-5578-40bd-b51b-88dc029265ff/resource/63b640e4-5501-4a6d-acaa-f2b654b147ee/download/prk_fpanv_m_gdo_20180101_20181221_t.zip
  format: null
  id: resource_63b640e4
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: prk_fpanv_m_gdo_20180101_20181221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Democratic People''s Republic of Korea: Copernicus Vegetation Index
    Anomaly (FAPAR Anomaly) (Data from 2017-01-01 to 2017-12-31)'
  download_url: https://data.humdata.org/dataset/1e3e1610-5578-40bd-b51b-88dc029265ff/resource/a10e0134-4d47-41cc-83ec-aff087254608/download/prk_fpanv_m_gdo_20170101_20171221_t.zip
  format: null
  id: resource_a10e0134
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: prk_fpanv_m_gdo_20170101_20171221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Democratic People''s Republic of Korea: Copernicus Vegetation Index
    Anomaly (FAPAR Anomaly) (Data from 2016-01-01 to 2016-12-31)'
  download_url: https://data.humdata.org/dataset/1e3e1610-5578-40bd-b51b-88dc029265ff/resource/b66d8b04-83f0-4442-aee1-76d62d7fcb90/download/prk_fpanv_m_gdo_20160101_20161221_t.zip
  format: null
  id: resource_b66d8b04
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: prk_fpanv_m_gdo_20160101_20161221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Democratic People''s Republic of Korea: Copernicus Vegetation Index
    Anomaly (FAPAR Anomaly) (Data from 2015-01-01 to 2015-12-31)'
  download_url: https://data.humdata.org/dataset/1e3e1610-5578-40bd-b51b-88dc029265ff/resource/5e0159f3-b0e4-4587-a140-60bfa1ea406c/download/prk_fpanv_m_gdo_20150101_20151221_t.zip
  format: null
  id: resource_5e0159f3
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: prk_fpanv_m_gdo_20150101_20151221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Democratic People''s Republic of Korea: Copernicus Vegetation Index
    Anomaly (FAPAR Anomaly) (Data from 2014-01-01 to 2014-12-31)'
  download_url: https://data.humdata.org/dataset/1e3e1610-5578-40bd-b51b-88dc029265ff/resource/abd55c1b-4abd-4a0f-8c34-62c52c8f4021/download/prk_fpanv_m_gdo_20140101_20141221_t.zip
  format: null
  id: resource_abd55c1b
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: prk_fpanv_m_gdo_20140101_20141221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Democratic People''s Republic of Korea: Copernicus Vegetation Index
    Anomaly (FAPAR Anomaly) (Data from 2013-01-01 to 2013-12-31)'
  download_url: https://data.humdata.org/dataset/1e3e1610-5578-40bd-b51b-88dc029265ff/resource/8517a121-e6bd-43fe-bee1-074ee0ef9bf6/download/prk_fpanv_m_gdo_20130101_20131221_t.zip
  format: null
  id: resource_8517a121
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: prk_fpanv_m_gdo_20130101_20131221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Democratic People''s Republic of Korea: Copernicus Vegetation Index
    Anomaly (FAPAR Anomaly) (Data from 2012-01-21 to 2012-12-31)'
  download_url: https://data.humdata.org/dataset/1e3e1610-5578-40bd-b51b-88dc029265ff/resource/fc08e777-3439-488d-a4c4-51ba232f34e0/download/prk_fpanv_m_gdo_20120121_20121221_t.zip
  format: null
  id: resource_fc08e777
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: prk_fpanv_m_gdo_20120121_20121221_t.zip
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-prk_copernicus_democraticpeoplesrepublic_2012
spatial:
  bbox: null
  centroid: null
  countries:
  - PRK
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2026-01-10'
  start: '2012-01-21'
temporal_resolution: null
title: 'Democratic People''s Republic of Korea: Copernicus Vegetation Index Anomaly
  (FAPAR Anomaly)'
version: null
vulnerability: null
---
