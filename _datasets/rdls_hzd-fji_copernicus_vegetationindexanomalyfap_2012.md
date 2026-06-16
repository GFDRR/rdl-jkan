---
attributions:
- entity:
    affiliation: null
    email: null
    name: Copernicus / European Commission Joint Research Centre (JRC)
    url: https://data.humdata.org/dataset/fji-anomalies-fapar-viirs
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Copernicus
  url: https://data.humdata.org/dataset/fji-anomalies-fapar-viirs
creator:
  affiliation: null
  email: null
  name: Copernicus
  url: https://data.humdata.org/dataset/fji-anomalies-fapar-viirs
dataset_id: rdls_hzd-fji_copernicus_vegetationindexanomalyfap_2012
description: 'Fraction of Absorbed Photosynthetically Active Radiation (FAPAR) is
  a biophysical dimensionless quantity (its values range from 0/no absorption to 1/total
  absorption) used to assess the greenness and health of vegetation. FAPAR anomalies
  can be used as an indicator to detect and monitor the impacts of agricultural drought
  on the growth and productivity of vegetation. The data is presented in 10-day time
  composite of the Visible Infrared Imaging Radiometer Suite (VIIRS).. [Source: This
  metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/fji-anomalies-fapar-viirs]'
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
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: FAPAR values from VIIRS satellite observations are composited at 10-day
    intervals. Anomalies are calculated at each grid cell by computing the deviation
    from a long-term mean baseline (2012 to the last available full year), producing
    raster datasets that serve as empirical indicators of agricultural drought stress
    on vegetation.
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
- href: https://data.humdata.org/dataset/fji-anomalies-fapar-viirs
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
  description: 'Fiji: Copernicus Vegetation Index Anomaly (FAPAR Anomaly) (Data from
    2026-01-01 to 2026-01-10)'
  download_url: https://data.humdata.org/dataset/ade3dbee-43b1-4726-97d7-5aaeb33ffd9b/resource/d4381781-0c12-4f17-b606-043c601698ed/download/fji_fpanv_m_gdo_20260101_20260101_t.zip
  format: null
  id: resource_d4381781
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: fji_fpanv_m_gdo_20260101_20260101_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Fiji: Copernicus Vegetation Index Anomaly (FAPAR Anomaly) (Data from
    2025-01-01 to 2025-12-31)'
  download_url: https://data.humdata.org/dataset/ade3dbee-43b1-4726-97d7-5aaeb33ffd9b/resource/ca9aeb0e-4b3b-47a7-a015-5374e9979f65/download/fji_fpanv_m_gdo_20250101_20251221_t.zip
  format: null
  id: resource_ca9aeb0e
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: fji_fpanv_m_gdo_20250101_20251221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Fiji: Copernicus Vegetation Index Anomaly (FAPAR Anomaly) (Data from
    2024-01-01 to 2024-12-31)'
  download_url: https://data.humdata.org/dataset/ade3dbee-43b1-4726-97d7-5aaeb33ffd9b/resource/aafd744c-f7bd-4e8e-8ce1-f4d98563d45f/download/fji_fpanv_m_gdo_20240101_20241221_t.zip
  format: null
  id: resource_aafd744c
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: fji_fpanv_m_gdo_20240101_20241221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Fiji: Copernicus Vegetation Index Anomaly (FAPAR Anomaly) (Data from
    2023-01-01 to 2023-12-31)'
  download_url: https://data.humdata.org/dataset/ade3dbee-43b1-4726-97d7-5aaeb33ffd9b/resource/810fbe76-6b38-4945-9f3f-2ad82625dfa3/download/fji_fpanv_m_gdo_20230101_20231221_t.zip
  format: null
  id: resource_810fbe76
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: fji_fpanv_m_gdo_20230101_20231221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Fiji: Copernicus Vegetation Index Anomaly (FAPAR Anomaly) (Data from
    2022-01-01 to 2022-12-31)'
  download_url: https://data.humdata.org/dataset/ade3dbee-43b1-4726-97d7-5aaeb33ffd9b/resource/1144b0b4-d706-4906-9d70-4e8692eb5225/download/fji_fpanv_m_gdo_20220101_20221221_t.zip
  format: null
  id: resource_1144b0b4
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: fji_fpanv_m_gdo_20220101_20221221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Fiji: Copernicus Vegetation Index Anomaly (FAPAR Anomaly) (Data from
    2021-01-01 to 2021-12-31)'
  download_url: https://data.humdata.org/dataset/ade3dbee-43b1-4726-97d7-5aaeb33ffd9b/resource/a23fb9a9-ff1e-4a6e-bf28-6854cbb5d309/download/fji_fpanv_m_gdo_20210101_20211221_t.zip
  format: null
  id: resource_a23fb9a9
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: fji_fpanv_m_gdo_20210101_20211221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Fiji: Copernicus Vegetation Index Anomaly (FAPAR Anomaly) (Data from
    2020-01-01 to 2020-12-31)'
  download_url: https://data.humdata.org/dataset/ade3dbee-43b1-4726-97d7-5aaeb33ffd9b/resource/2974be72-5d78-4508-bece-44b1e154f42d/download/fji_fpanv_m_gdo_20200101_20201221_t.zip
  format: null
  id: resource_2974be72
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: fji_fpanv_m_gdo_20200101_20201221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Fiji: Copernicus Vegetation Index Anomaly (FAPAR Anomaly) (Data from
    2019-01-01 to 2019-12-31)'
  download_url: https://data.humdata.org/dataset/ade3dbee-43b1-4726-97d7-5aaeb33ffd9b/resource/89a24379-0b08-4e61-b5b2-e43cf62232a8/download/fji_fpanv_m_gdo_20190101_20191221_t.zip
  format: null
  id: resource_89a24379
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: fji_fpanv_m_gdo_20190101_20191221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Fiji: Copernicus Vegetation Index Anomaly (FAPAR Anomaly) (Data from
    2018-01-01 to 2018-12-31)'
  download_url: https://data.humdata.org/dataset/ade3dbee-43b1-4726-97d7-5aaeb33ffd9b/resource/89848797-96ce-42bc-929c-60ae3879a649/download/fji_fpanv_m_gdo_20180101_20181221_t.zip
  format: null
  id: resource_89848797
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: fji_fpanv_m_gdo_20180101_20181221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Fiji: Copernicus Vegetation Index Anomaly (FAPAR Anomaly) (Data from
    2017-01-01 to 2017-12-31)'
  download_url: https://data.humdata.org/dataset/ade3dbee-43b1-4726-97d7-5aaeb33ffd9b/resource/ef5df976-d393-47c0-b348-6ead3488f480/download/fji_fpanv_m_gdo_20170101_20171221_t.zip
  format: null
  id: resource_ef5df976
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: fji_fpanv_m_gdo_20170101_20171221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Fiji: Copernicus Vegetation Index Anomaly (FAPAR Anomaly) (Data from
    2016-01-01 to 2016-12-31)'
  download_url: https://data.humdata.org/dataset/ade3dbee-43b1-4726-97d7-5aaeb33ffd9b/resource/33205667-616f-46de-9ead-4d9086edf0a9/download/fji_fpanv_m_gdo_20160101_20161221_t.zip
  format: null
  id: resource_33205667
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: fji_fpanv_m_gdo_20160101_20161221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Fiji: Copernicus Vegetation Index Anomaly (FAPAR Anomaly) (Data from
    2015-01-01 to 2015-12-31)'
  download_url: https://data.humdata.org/dataset/ade3dbee-43b1-4726-97d7-5aaeb33ffd9b/resource/c322a895-d9db-4e9e-8289-b9de7073a53b/download/fji_fpanv_m_gdo_20150101_20151221_t.zip
  format: null
  id: resource_c322a895
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: fji_fpanv_m_gdo_20150101_20151221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Fiji: Copernicus Vegetation Index Anomaly (FAPAR Anomaly) (Data from
    2014-01-01 to 2014-12-31)'
  download_url: https://data.humdata.org/dataset/ade3dbee-43b1-4726-97d7-5aaeb33ffd9b/resource/3dfdeae8-2e9d-46ff-bf09-c69c03ab09a5/download/fji_fpanv_m_gdo_20140101_20141221_t.zip
  format: null
  id: resource_3dfdeae8
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: fji_fpanv_m_gdo_20140101_20141221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Fiji: Copernicus Vegetation Index Anomaly (FAPAR Anomaly) (Data from
    2013-01-01 to 2013-12-31)'
  download_url: https://data.humdata.org/dataset/ade3dbee-43b1-4726-97d7-5aaeb33ffd9b/resource/78cae389-d477-44d5-8b70-885cedb49350/download/fji_fpanv_m_gdo_20130101_20131221_t.zip
  format: null
  id: resource_78cae389
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: fji_fpanv_m_gdo_20130101_20131221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Fiji: Copernicus Vegetation Index Anomaly (FAPAR Anomaly) (Data from
    2012-01-21 to 2012-12-31)'
  download_url: https://data.humdata.org/dataset/ade3dbee-43b1-4726-97d7-5aaeb33ffd9b/resource/d7fe8ee3-98ff-4146-a8ab-5cb68a6d9940/download/fji_fpanv_m_gdo_20120121_20121221_t.zip
  format: null
  id: resource_d7fe8ee3
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: fji_fpanv_m_gdo_20120121_20121221_t.zip
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-fji_copernicus_vegetationindexanomalyfap_2012
spatial:
  bbox: null
  centroid: null
  countries:
  - FJI
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2026-01-10'
  start: '2012-01-21'
temporal_resolution: null
title: 'Fiji: Copernicus Vegetation Index Anomaly (FAPAR Anomaly)'
version: null
vulnerability: null
---
