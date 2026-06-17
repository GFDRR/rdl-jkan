---
attributions:
- entity:
    affiliation: null
    email: null
    name: Copernicus / European Commission Joint Research Centre (JRC)
    url: https://data.humdata.org/dataset/usa-anomalies-fapar-viirs
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Copernicus
  url: https://data.humdata.org/dataset/usa-anomalies-fapar-viirs
creator:
  affiliation: null
  email: null
  name: Copernicus
  url: https://data.humdata.org/dataset/usa-anomalies-fapar-viirs
dataset_id: rdls_hzd-usa_copernicus_americavegetationindexano_2012
description: 'Fraction of Absorbed Photosynthetically Active Radiation (FAPAR) is
  a biophysical dimensionless quantity (its values range from 0/no absorption to 1/total
  absorption) used to assess the greenness and health of vegetation. FAPAR anomalies
  can be used as an indicator to detect and monitor the impacts of agricultural drought
  on the growth and productivity of vegetation. The data is presented in 10-day time
  composite of the Visible Infrared Imaging Radiometer Suite (VIIRS).. [Source: This
  metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/usa-anomalies-fapar-viirs]'
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
  description: FAPAR values from VIIRS satellite radiometer observations are composited
    at 10-day intervals. Anomalies are calculated at each grid cell as the deviation
    from a long-term mean baseline (2012 to the last available full year), producing
    raster datasets that serve as empirical indicators of agricultural drought impacts
    on vegetation productivity across the United States.
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
- href: https://data.humdata.org/dataset/usa-anomalies-fapar-viirs
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
  description: 'United States of America: Copernicus Vegetation Index Anomaly (FAPAR
    Anomaly) (Data from 2026-01-01 to 2026-01-10)'
  download_url: https://data.humdata.org/dataset/2a013d2d-067c-4d57-8beb-927a87288309/resource/6f3d42f6-66b5-411c-97eb-7bb9dd0a23bc/download/usa_fpanv_m_gdo_20260101_20260101_t.zip
  format: null
  id: resource_6f3d42f6
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: usa_fpanv_m_gdo_20260101_20260101_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'United States of America: Copernicus Vegetation Index Anomaly (FAPAR
    Anomaly) (Data from 2025-01-01 to 2025-12-31)'
  download_url: https://data.humdata.org/dataset/2a013d2d-067c-4d57-8beb-927a87288309/resource/4026f3df-6872-4446-b2da-674d3ca9e1f3/download/usa_fpanv_m_gdo_20250101_20251221_t.zip
  format: null
  id: resource_4026f3df
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: usa_fpanv_m_gdo_20250101_20251221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'United States of America: Copernicus Vegetation Index Anomaly (FAPAR
    Anomaly) (Data from 2024-01-01 to 2024-12-31)'
  download_url: https://data.humdata.org/dataset/2a013d2d-067c-4d57-8beb-927a87288309/resource/cbe462f0-cdee-477e-b76f-be0eafc6b6ff/download/usa_fpanv_m_gdo_20240101_20241221_t.zip
  format: null
  id: resource_cbe462f0
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: usa_fpanv_m_gdo_20240101_20241221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'United States of America: Copernicus Vegetation Index Anomaly (FAPAR
    Anomaly) (Data from 2023-01-01 to 2023-12-31)'
  download_url: https://data.humdata.org/dataset/2a013d2d-067c-4d57-8beb-927a87288309/resource/31251ca4-e56c-434b-894d-861c1365feeb/download/usa_fpanv_m_gdo_20230101_20231221_t.zip
  format: null
  id: resource_31251ca4
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: usa_fpanv_m_gdo_20230101_20231221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'United States of America: Copernicus Vegetation Index Anomaly (FAPAR
    Anomaly) (Data from 2022-01-01 to 2022-12-31)'
  download_url: https://data.humdata.org/dataset/2a013d2d-067c-4d57-8beb-927a87288309/resource/40defac3-4ec8-4ea9-aae9-980135e0e70c/download/usa_fpanv_m_gdo_20220101_20221221_t.zip
  format: null
  id: resource_40defac3
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: usa_fpanv_m_gdo_20220101_20221221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'United States of America: Copernicus Vegetation Index Anomaly (FAPAR
    Anomaly) (Data from 2021-01-01 to 2021-12-31)'
  download_url: https://data.humdata.org/dataset/2a013d2d-067c-4d57-8beb-927a87288309/resource/03fb506d-cf5e-445e-922a-fe7fceb1462f/download/usa_fpanv_m_gdo_20210101_20211221_t.zip
  format: null
  id: resource_03fb506d
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: usa_fpanv_m_gdo_20210101_20211221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'United States of America: Copernicus Vegetation Index Anomaly (FAPAR
    Anomaly) (Data from 2020-01-01 to 2020-12-31)'
  download_url: https://data.humdata.org/dataset/2a013d2d-067c-4d57-8beb-927a87288309/resource/ae209e16-55f8-4514-b997-9a51d0f1b7c0/download/usa_fpanv_m_gdo_20200101_20201221_t.zip
  format: null
  id: resource_ae209e16
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: usa_fpanv_m_gdo_20200101_20201221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'United States of America: Copernicus Vegetation Index Anomaly (FAPAR
    Anomaly) (Data from 2019-01-01 to 2019-12-31)'
  download_url: https://data.humdata.org/dataset/2a013d2d-067c-4d57-8beb-927a87288309/resource/5bfe004e-4299-412a-ac17-56cc313f8496/download/usa_fpanv_m_gdo_20190101_20191221_t.zip
  format: null
  id: resource_5bfe004e
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: usa_fpanv_m_gdo_20190101_20191221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'United States of America: Copernicus Vegetation Index Anomaly (FAPAR
    Anomaly) (Data from 2018-01-01 to 2018-12-31)'
  download_url: https://data.humdata.org/dataset/2a013d2d-067c-4d57-8beb-927a87288309/resource/d22f33b7-68ac-4ceb-8da1-967ddb89fb36/download/usa_fpanv_m_gdo_20180101_20181221_t.zip
  format: null
  id: resource_d22f33b7
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: usa_fpanv_m_gdo_20180101_20181221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'United States of America: Copernicus Vegetation Index Anomaly (FAPAR
    Anomaly) (Data from 2017-01-01 to 2017-12-31)'
  download_url: https://data.humdata.org/dataset/2a013d2d-067c-4d57-8beb-927a87288309/resource/d19bef8d-406d-46a7-9d39-bf47c3e778e2/download/usa_fpanv_m_gdo_20170101_20171221_t.zip
  format: null
  id: resource_d19bef8d
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: usa_fpanv_m_gdo_20170101_20171221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'United States of America: Copernicus Vegetation Index Anomaly (FAPAR
    Anomaly) (Data from 2016-01-01 to 2016-12-31)'
  download_url: https://data.humdata.org/dataset/2a013d2d-067c-4d57-8beb-927a87288309/resource/2f425754-3de7-436e-be1f-60ae5422b12b/download/usa_fpanv_m_gdo_20160101_20161221_t.zip
  format: null
  id: resource_2f425754
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: usa_fpanv_m_gdo_20160101_20161221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'United States of America: Copernicus Vegetation Index Anomaly (FAPAR
    Anomaly) (Data from 2015-01-01 to 2015-12-31)'
  download_url: https://data.humdata.org/dataset/2a013d2d-067c-4d57-8beb-927a87288309/resource/35bfe68b-8eb3-41e8-8598-3f8d66029993/download/usa_fpanv_m_gdo_20150101_20151221_t.zip
  format: null
  id: resource_35bfe68b
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: usa_fpanv_m_gdo_20150101_20151221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'United States of America: Copernicus Vegetation Index Anomaly (FAPAR
    Anomaly) (Data from 2014-01-01 to 2014-12-31)'
  download_url: https://data.humdata.org/dataset/2a013d2d-067c-4d57-8beb-927a87288309/resource/ebedefc3-c636-4e42-99b0-90872e26dca3/download/usa_fpanv_m_gdo_20140101_20141221_t.zip
  format: null
  id: resource_ebedefc3
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: usa_fpanv_m_gdo_20140101_20141221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'United States of America: Copernicus Vegetation Index Anomaly (FAPAR
    Anomaly) (Data from 2013-01-01 to 2013-12-31)'
  download_url: https://data.humdata.org/dataset/2a013d2d-067c-4d57-8beb-927a87288309/resource/404ac2b4-ce46-44ad-8ca2-51d63e389118/download/usa_fpanv_m_gdo_20130101_20131221_t.zip
  format: null
  id: resource_404ac2b4
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: usa_fpanv_m_gdo_20130101_20131221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'United States of America: Copernicus Vegetation Index Anomaly (FAPAR
    Anomaly) (Data from 2012-01-21 to 2012-12-31)'
  download_url: https://data.humdata.org/dataset/2a013d2d-067c-4d57-8beb-927a87288309/resource/c7495079-9e52-49df-83e2-3062a285411e/download/usa_fpanv_m_gdo_20120121_20121221_t.zip
  format: null
  id: resource_c7495079
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: usa_fpanv_m_gdo_20120121_20121221_t.zip
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-usa_copernicus_americavegetationindexano_2012
spatial:
  bbox: null
  centroid: null
  countries:
  - USA
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2026-01-10'
  start: '2012-01-21'
temporal_resolution: null
title: 'United States of America: Copernicus Vegetation Index Anomaly (FAPAR Anomaly)'
version: null
vulnerability: null
---
