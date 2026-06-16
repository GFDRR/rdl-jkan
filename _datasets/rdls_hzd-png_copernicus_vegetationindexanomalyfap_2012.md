---
attributions:
- entity:
    affiliation: null
    email: null
    name: Copernicus / European Commission Joint Research Centre (JRC)
    url: https://data.humdata.org/dataset/png-anomalies-fapar-viirs
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Copernicus
  url: https://data.humdata.org/dataset/png-anomalies-fapar-viirs
creator:
  affiliation: null
  email: null
  name: Copernicus
  url: https://data.humdata.org/dataset/png-anomalies-fapar-viirs
dataset_id: rdls_hzd-png_copernicus_vegetationindexanomalyfap_2012
description: 'Fraction of Absorbed Photosynthetically Active Radiation (FAPAR) is
  a biophysical dimensionless quantity (its values range from 0/no absorption to 1/total
  absorption) used to assess the greenness and health of vegetation. FAPAR anomalies
  can be used as an indicator to detect and monitor the impacts of agricultural drought
  on the growth and productivity of vegetation. The data is presented in 10-day time
  composite of the Visible Infrared Imaging Radiometer Suite (VIIRS).. [Source: This
  metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/png-anomalies-fapar-viirs]'
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
  description: FAPAR values from VIIRS satellite radiometer observations are composited
    at 10-day intervals. Anomalies are calculated at each grid cell as the deviation
    from a long-term mean baseline (2012 to the last complete year), producing raster
    datasets that serve as an empirical indicator of agricultural drought stress on
    vegetation across Papua New Guinea.
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
- href: https://data.humdata.org/dataset/png-anomalies-fapar-viirs
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
  description: 'Papua New Guinea: Copernicus Vegetation Index Anomaly (FAPAR Anomaly)
    (Data from 2026-01-01 to 2026-01-10)'
  download_url: https://data.humdata.org/dataset/bd5bca58-b834-45eb-88b4-e4dac3f25a11/resource/ff575522-18e2-4e1d-bf7a-0eb106b73fb3/download/png_fpanv_m_gdo_20260101_20260101_t.zip
  format: null
  id: resource_ff575522
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: png_fpanv_m_gdo_20260101_20260101_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Papua New Guinea: Copernicus Vegetation Index Anomaly (FAPAR Anomaly)
    (Data from 2025-01-01 to 2025-12-31)'
  download_url: https://data.humdata.org/dataset/bd5bca58-b834-45eb-88b4-e4dac3f25a11/resource/4b180d1f-0e3f-45b2-bc3e-2ef724f57cac/download/png_fpanv_m_gdo_20250101_20251221_t.zip
  format: null
  id: resource_4b180d1f
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: png_fpanv_m_gdo_20250101_20251221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Papua New Guinea: Copernicus Vegetation Index Anomaly (FAPAR Anomaly)
    (Data from 2024-01-01 to 2024-12-31)'
  download_url: https://data.humdata.org/dataset/bd5bca58-b834-45eb-88b4-e4dac3f25a11/resource/65546e30-58c3-45c4-be7f-2302b65ad00f/download/png_fpanv_m_gdo_20240101_20241221_t.zip
  format: null
  id: resource_65546e30
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: png_fpanv_m_gdo_20240101_20241221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Papua New Guinea: Copernicus Vegetation Index Anomaly (FAPAR Anomaly)
    (Data from 2023-01-01 to 2023-12-31)'
  download_url: https://data.humdata.org/dataset/bd5bca58-b834-45eb-88b4-e4dac3f25a11/resource/9c8dc21b-75c6-43ba-a6e1-36f8d9ccd9d1/download/png_fpanv_m_gdo_20230101_20231221_t.zip
  format: null
  id: resource_9c8dc21b
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: png_fpanv_m_gdo_20230101_20231221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Papua New Guinea: Copernicus Vegetation Index Anomaly (FAPAR Anomaly)
    (Data from 2022-01-01 to 2022-12-31)'
  download_url: https://data.humdata.org/dataset/bd5bca58-b834-45eb-88b4-e4dac3f25a11/resource/c3cceffe-79ab-42c2-8e33-2f8fa8b58711/download/png_fpanv_m_gdo_20220101_20221221_t.zip
  format: null
  id: resource_c3cceffe
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: png_fpanv_m_gdo_20220101_20221221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Papua New Guinea: Copernicus Vegetation Index Anomaly (FAPAR Anomaly)
    (Data from 2021-01-01 to 2021-12-31)'
  download_url: https://data.humdata.org/dataset/bd5bca58-b834-45eb-88b4-e4dac3f25a11/resource/1d7986ad-fed0-458d-a020-f0d2e5acfb5e/download/png_fpanv_m_gdo_20210101_20211221_t.zip
  format: null
  id: resource_1d7986ad
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: png_fpanv_m_gdo_20210101_20211221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Papua New Guinea: Copernicus Vegetation Index Anomaly (FAPAR Anomaly)
    (Data from 2020-01-01 to 2020-12-31)'
  download_url: https://data.humdata.org/dataset/bd5bca58-b834-45eb-88b4-e4dac3f25a11/resource/185932c3-5c77-4ea7-9238-0bdb7b5d65d2/download/png_fpanv_m_gdo_20200101_20201221_t.zip
  format: null
  id: resource_185932c3
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: png_fpanv_m_gdo_20200101_20201221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Papua New Guinea: Copernicus Vegetation Index Anomaly (FAPAR Anomaly)
    (Data from 2019-01-01 to 2019-12-31)'
  download_url: https://data.humdata.org/dataset/bd5bca58-b834-45eb-88b4-e4dac3f25a11/resource/e30d20a7-2532-4747-9b37-3340cb9c8146/download/png_fpanv_m_gdo_20190101_20191221_t.zip
  format: null
  id: resource_e30d20a7
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: png_fpanv_m_gdo_20190101_20191221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Papua New Guinea: Copernicus Vegetation Index Anomaly (FAPAR Anomaly)
    (Data from 2018-01-01 to 2018-12-31)'
  download_url: https://data.humdata.org/dataset/bd5bca58-b834-45eb-88b4-e4dac3f25a11/resource/25b4a40b-f65d-4c49-a9ff-31083888e2d5/download/png_fpanv_m_gdo_20180101_20181221_t.zip
  format: null
  id: resource_25b4a40b
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: png_fpanv_m_gdo_20180101_20181221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Papua New Guinea: Copernicus Vegetation Index Anomaly (FAPAR Anomaly)
    (Data from 2017-01-01 to 2017-12-31)'
  download_url: https://data.humdata.org/dataset/bd5bca58-b834-45eb-88b4-e4dac3f25a11/resource/334c80ed-ca1d-4904-9654-02e4bc964d29/download/png_fpanv_m_gdo_20170101_20171221_t.zip
  format: null
  id: resource_334c80ed
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: png_fpanv_m_gdo_20170101_20171221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Papua New Guinea: Copernicus Vegetation Index Anomaly (FAPAR Anomaly)
    (Data from 2016-01-01 to 2016-12-31)'
  download_url: https://data.humdata.org/dataset/bd5bca58-b834-45eb-88b4-e4dac3f25a11/resource/a8947822-62dd-4e7e-abbd-06c4082afbbd/download/png_fpanv_m_gdo_20160101_20161221_t.zip
  format: null
  id: resource_a8947822
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: png_fpanv_m_gdo_20160101_20161221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Papua New Guinea: Copernicus Vegetation Index Anomaly (FAPAR Anomaly)
    (Data from 2015-01-01 to 2015-12-31)'
  download_url: https://data.humdata.org/dataset/bd5bca58-b834-45eb-88b4-e4dac3f25a11/resource/d9db4f5d-144b-4a11-8ef9-ed3a25aefd30/download/png_fpanv_m_gdo_20150101_20151221_t.zip
  format: null
  id: resource_d9db4f5d
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: png_fpanv_m_gdo_20150101_20151221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Papua New Guinea: Copernicus Vegetation Index Anomaly (FAPAR Anomaly)
    (Data from 2014-01-01 to 2014-12-31)'
  download_url: https://data.humdata.org/dataset/bd5bca58-b834-45eb-88b4-e4dac3f25a11/resource/e1ba3013-1cc9-4841-9c1a-7c9effd15091/download/png_fpanv_m_gdo_20140101_20141221_t.zip
  format: null
  id: resource_e1ba3013
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: png_fpanv_m_gdo_20140101_20141221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Papua New Guinea: Copernicus Vegetation Index Anomaly (FAPAR Anomaly)
    (Data from 2013-01-01 to 2013-12-31)'
  download_url: https://data.humdata.org/dataset/bd5bca58-b834-45eb-88b4-e4dac3f25a11/resource/944e62c9-9f6c-490c-86e7-62e532a020a5/download/png_fpanv_m_gdo_20130101_20131221_t.zip
  format: null
  id: resource_944e62c9
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: png_fpanv_m_gdo_20130101_20131221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Papua New Guinea: Copernicus Vegetation Index Anomaly (FAPAR Anomaly)
    (Data from 2012-01-21 to 2012-12-31)'
  download_url: https://data.humdata.org/dataset/bd5bca58-b834-45eb-88b4-e4dac3f25a11/resource/746edffc-d478-4a10-abad-0801bc4176c5/download/png_fpanv_m_gdo_20120121_20121221_t.zip
  format: null
  id: resource_746edffc
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: png_fpanv_m_gdo_20120121_20121221_t.zip
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-png_copernicus_vegetationindexanomalyfap_2012
spatial:
  bbox: null
  centroid: null
  countries:
  - PNG
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2026-01-10'
  start: '2012-01-21'
temporal_resolution: null
title: 'Papua New Guinea: Copernicus Vegetation Index Anomaly (FAPAR Anomaly)'
version: null
vulnerability: null
---
