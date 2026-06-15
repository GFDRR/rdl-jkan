---
attributions:
- entity:
    affiliation: null
    email: null
    name: Copernicus Vegetation Index (VIIRS)
    url: https://data.humdata.org/dataset/gbr-anomalies-fapar-viirs
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Copernicus
  url: https://data.humdata.org/dataset/gbr-anomalies-fapar-viirs
creator:
  affiliation: null
  email: null
  name: Copernicus
  url: https://data.humdata.org/dataset/gbr-anomalies-fapar-viirs
dataset_id: rdls_hzd-gbr_copernicus_northernirelandvegetation_2012
description: 'Fraction of Absorbed Photosynthetically Active Radiation (FAPAR) is
  a biophysical dimensionless quantity (its values range from 0/no absorption to 1/total
  absorption) used to assess the greenness and health of vegetation. FAPAR anomalies
  can be used as an indicator to detect and monitor the impacts of agricultural drought
  on the growth and productivity of vegetation. The data is presented in 10-day time
  composite of the Visible Infrared Imaging Radiometer Suite (VIIRS).. [Source: This
  metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/gbr-anomalies-fapar-viirs]'
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
  description: FAPAR values from VIIRS satellite observations are composited at 10-day
    intervals. Anomalies are calculated at each grid cell by computing the deviation
    from a long-term mean baseline spanning 2012 to the most recent complete year,
    enabling detection of agricultural drought impacts on vegetation productivity
    across the UK.
  sources:
  - id: source_1
    license: null
    name: Copernicus Vegetation Index (VIIRS)
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/gbr-anomalies-fapar-viirs
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
  description: 'United Kingdom of Great Britain and Northern Ireland: Copernicus Vegetation
    Index Anomaly (FAPAR Anomaly) (Data from 2026-01-01 to 2026-01-10)'
  download_url: https://data.humdata.org/dataset/fce09f2a-d646-4d0d-a8b4-b5513c699e09/resource/a7cf7332-ecee-41f0-81d5-6a4f01a8b0a0/download/gbr_fpanv_m_gdo_20260101_20260101_t.zip
  format: null
  id: resource_a7cf7332
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gbr_fpanv_m_gdo_20260101_20260101_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'United Kingdom of Great Britain and Northern Ireland: Copernicus Vegetation
    Index Anomaly (FAPAR Anomaly) (Data from 2025-01-01 to 2025-12-31)'
  download_url: https://data.humdata.org/dataset/fce09f2a-d646-4d0d-a8b4-b5513c699e09/resource/59ca314f-af3c-4175-883e-5ed9c000f7ef/download/gbr_fpanv_m_gdo_20250101_20251221_t.zip
  format: null
  id: resource_59ca314f
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gbr_fpanv_m_gdo_20250101_20251221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'United Kingdom of Great Britain and Northern Ireland: Copernicus Vegetation
    Index Anomaly (FAPAR Anomaly) (Data from 2024-01-01 to 2024-12-31)'
  download_url: https://data.humdata.org/dataset/fce09f2a-d646-4d0d-a8b4-b5513c699e09/resource/9f098dcd-f69d-40ad-aff7-081fcb594f52/download/gbr_fpanv_m_gdo_20240101_20241221_t.zip
  format: null
  id: resource_9f098dcd
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gbr_fpanv_m_gdo_20240101_20241221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'United Kingdom of Great Britain and Northern Ireland: Copernicus Vegetation
    Index Anomaly (FAPAR Anomaly) (Data from 2023-01-01 to 2023-12-31)'
  download_url: https://data.humdata.org/dataset/fce09f2a-d646-4d0d-a8b4-b5513c699e09/resource/7415a198-d697-4f3e-9921-7c683e87128a/download/gbr_fpanv_m_gdo_20230101_20231221_t.zip
  format: null
  id: resource_7415a198
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gbr_fpanv_m_gdo_20230101_20231221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'United Kingdom of Great Britain and Northern Ireland: Copernicus Vegetation
    Index Anomaly (FAPAR Anomaly) (Data from 2022-01-01 to 2022-12-31)'
  download_url: https://data.humdata.org/dataset/fce09f2a-d646-4d0d-a8b4-b5513c699e09/resource/31f263eb-7dfc-4f18-9e03-f75b8bce34e0/download/gbr_fpanv_m_gdo_20220101_20221221_t.zip
  format: null
  id: resource_31f263eb
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gbr_fpanv_m_gdo_20220101_20221221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'United Kingdom of Great Britain and Northern Ireland: Copernicus Vegetation
    Index Anomaly (FAPAR Anomaly) (Data from 2021-01-01 to 2021-12-31)'
  download_url: https://data.humdata.org/dataset/fce09f2a-d646-4d0d-a8b4-b5513c699e09/resource/c8e9f884-4b1e-48a4-a3c2-14c9a3e21873/download/gbr_fpanv_m_gdo_20210101_20211221_t.zip
  format: null
  id: resource_c8e9f884
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gbr_fpanv_m_gdo_20210101_20211221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'United Kingdom of Great Britain and Northern Ireland: Copernicus Vegetation
    Index Anomaly (FAPAR Anomaly) (Data from 2020-01-01 to 2020-12-31)'
  download_url: https://data.humdata.org/dataset/fce09f2a-d646-4d0d-a8b4-b5513c699e09/resource/4a452105-b4d0-4f5d-97f4-0daf2cdb750c/download/gbr_fpanv_m_gdo_20200101_20201221_t.zip
  format: null
  id: resource_4a452105
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gbr_fpanv_m_gdo_20200101_20201221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'United Kingdom of Great Britain and Northern Ireland: Copernicus Vegetation
    Index Anomaly (FAPAR Anomaly) (Data from 2019-01-01 to 2019-12-31)'
  download_url: https://data.humdata.org/dataset/fce09f2a-d646-4d0d-a8b4-b5513c699e09/resource/bc2ecff1-6a8b-43ae-9ed0-d1c6434723b5/download/gbr_fpanv_m_gdo_20190101_20191221_t.zip
  format: null
  id: resource_bc2ecff1
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gbr_fpanv_m_gdo_20190101_20191221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'United Kingdom of Great Britain and Northern Ireland: Copernicus Vegetation
    Index Anomaly (FAPAR Anomaly) (Data from 2018-01-01 to 2018-12-31)'
  download_url: https://data.humdata.org/dataset/fce09f2a-d646-4d0d-a8b4-b5513c699e09/resource/4befbd0f-8dc9-4b64-909a-9c8fb564fb48/download/gbr_fpanv_m_gdo_20180101_20181221_t.zip
  format: null
  id: resource_4befbd0f
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gbr_fpanv_m_gdo_20180101_20181221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'United Kingdom of Great Britain and Northern Ireland: Copernicus Vegetation
    Index Anomaly (FAPAR Anomaly) (Data from 2017-01-01 to 2017-12-31)'
  download_url: https://data.humdata.org/dataset/fce09f2a-d646-4d0d-a8b4-b5513c699e09/resource/6a71f7e5-63ca-48c3-a575-77a38f3c5087/download/gbr_fpanv_m_gdo_20170101_20171221_t.zip
  format: null
  id: resource_6a71f7e5
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gbr_fpanv_m_gdo_20170101_20171221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'United Kingdom of Great Britain and Northern Ireland: Copernicus Vegetation
    Index Anomaly (FAPAR Anomaly) (Data from 2016-01-01 to 2016-12-31)'
  download_url: https://data.humdata.org/dataset/fce09f2a-d646-4d0d-a8b4-b5513c699e09/resource/353fd98d-73b4-4f08-abca-1fc137c9593e/download/gbr_fpanv_m_gdo_20160101_20161221_t.zip
  format: null
  id: resource_353fd98d
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gbr_fpanv_m_gdo_20160101_20161221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'United Kingdom of Great Britain and Northern Ireland: Copernicus Vegetation
    Index Anomaly (FAPAR Anomaly) (Data from 2015-01-01 to 2015-12-31)'
  download_url: https://data.humdata.org/dataset/fce09f2a-d646-4d0d-a8b4-b5513c699e09/resource/a80a5b1e-c804-4d01-bd73-95863667d078/download/gbr_fpanv_m_gdo_20150101_20151221_t.zip
  format: null
  id: resource_a80a5b1e
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gbr_fpanv_m_gdo_20150101_20151221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'United Kingdom of Great Britain and Northern Ireland: Copernicus Vegetation
    Index Anomaly (FAPAR Anomaly) (Data from 2014-01-01 to 2014-12-31)'
  download_url: https://data.humdata.org/dataset/fce09f2a-d646-4d0d-a8b4-b5513c699e09/resource/902102f5-7771-4b88-9b01-007f072b28e5/download/gbr_fpanv_m_gdo_20140101_20141221_t.zip
  format: null
  id: resource_902102f5
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gbr_fpanv_m_gdo_20140101_20141221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'United Kingdom of Great Britain and Northern Ireland: Copernicus Vegetation
    Index Anomaly (FAPAR Anomaly) (Data from 2013-01-01 to 2013-12-31)'
  download_url: https://data.humdata.org/dataset/fce09f2a-d646-4d0d-a8b4-b5513c699e09/resource/c48ceb6e-e1bb-462a-ae21-13a4d9ba6999/download/gbr_fpanv_m_gdo_20130101_20131221_t.zip
  format: null
  id: resource_c48ceb6e
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gbr_fpanv_m_gdo_20130101_20131221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'United Kingdom of Great Britain and Northern Ireland: Copernicus Vegetation
    Index Anomaly (FAPAR Anomaly) (Data from 2012-01-21 to 2012-12-31)'
  download_url: https://data.humdata.org/dataset/fce09f2a-d646-4d0d-a8b4-b5513c699e09/resource/25d5eb7d-6eab-4740-9b59-2e6256217333/download/gbr_fpanv_m_gdo_20120121_20121221_t.zip
  format: null
  id: resource_25d5eb7d
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gbr_fpanv_m_gdo_20120121_20121221_t.zip
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-gbr_copernicus_northernirelandvegetation_2012
spatial:
  bbox: null
  centroid: null
  countries:
  - GBR
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2026-01-10'
  start: '2012-01-21'
temporal_resolution: null
title: 'United Kingdom of Great Britain and Northern Ireland: Copernicus Vegetation
  Index Anomaly (FAPAR Anomaly)'
version: null
vulnerability: null
---
