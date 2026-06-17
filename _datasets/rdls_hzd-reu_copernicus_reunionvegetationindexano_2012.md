---
attributions:
- entity:
    affiliation: null
    email: null
    name: European Commission, Joint Research Centre (JRC)
    url: https://data.humdata.org/dataset/reu-anomalies-fapar-viirs
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Copernicus
  url: https://data.humdata.org/dataset/reu-anomalies-fapar-viirs
creator:
  affiliation: null
  email: null
  name: Copernicus
  url: https://data.humdata.org/dataset/reu-anomalies-fapar-viirs
dataset_id: rdls_hzd-reu_copernicus_reunionvegetationindexano_2012
description: 'Fraction of Absorbed Photosynthetically Active Radiation (FAPAR) is
  a biophysical dimensionless quantity (its values range from 0/no absorption to 1/total
  absorption) used to assess the greenness and health of vegetation. FAPAR anomalies
  can be used as an indicator to detect and monitor the impacts of agricultural drought
  on the growth and productivity of vegetation. The data is presented in 10-day time
  composite of the Visible Infrared Imaging Radiometer Suite (VIIRS).. [Source: This
  metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/reu-anomalies-fapar-viirs]'
details: Variations in the vegetation health and/or cover could be related to stress
  factors not related to droughts (e.g., plant diseases, pests, hail, flooding). To
  determine if changes in FAPAR are linked with a drought event or not, FAPAR data
  should be interpreted jointly with other indicators (as in the EDO Combined Drought
  Indicator).
exposure: []
hazard:
  event_sets:
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
  type: drought
license: CC-BY-4.0
lineage:
  description: FAPAR values from VIIRS satellite observations are composited at 10-day
    intervals. Anomalies are calculated at each grid cell as the deviation from a
    long-term mean baseline (2012 to last available full year), generating raster
    datasets in GeoTIFF format to enable detection and monitoring of agricultural
    drought impacts on vegetation productivity.
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
- href: https://data.humdata.org/dataset/reu-anomalies-fapar-viirs
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
  description: "R\xE9union: Copernicus Vegetation Index Anomaly (FAPAR Anomaly) (Data\
    \ from 2026-01-01 to 2026-01-10)"
  download_url: https://data.humdata.org/dataset/5d29e2a9-6ca9-4d94-a562-7d3595ce54c3/resource/34d80821-0afc-4226-9b3e-67d019d8ba99/download/reu_fpanv_m_gdo_20260101_20260101_t.zip
  format: null
  id: resource_34d80821
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: reu_fpanv_m_gdo_20260101_20260101_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "R\xE9union: Copernicus Vegetation Index Anomaly (FAPAR Anomaly) (Data\
    \ from 2025-01-01 to 2025-12-31)"
  download_url: https://data.humdata.org/dataset/5d29e2a9-6ca9-4d94-a562-7d3595ce54c3/resource/4b1dccba-5878-4c0d-9625-62a0fe4c4252/download/reu_fpanv_m_gdo_20250101_20251221_t.zip
  format: null
  id: resource_4b1dccba
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: reu_fpanv_m_gdo_20250101_20251221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "R\xE9union: Copernicus Vegetation Index Anomaly (FAPAR Anomaly) (Data\
    \ from 2024-01-01 to 2024-12-31)"
  download_url: https://data.humdata.org/dataset/5d29e2a9-6ca9-4d94-a562-7d3595ce54c3/resource/b80dcb4d-e28c-419f-a087-db364b4d8b70/download/reu_fpanv_m_gdo_20240101_20241221_t.zip
  format: null
  id: resource_b80dcb4d
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: reu_fpanv_m_gdo_20240101_20241221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "R\xE9union: Copernicus Vegetation Index Anomaly (FAPAR Anomaly) (Data\
    \ from 2023-01-01 to 2023-12-31)"
  download_url: https://data.humdata.org/dataset/5d29e2a9-6ca9-4d94-a562-7d3595ce54c3/resource/c7b6bd39-5486-4e29-903b-18bdad22f35d/download/reu_fpanv_m_gdo_20230101_20231221_t.zip
  format: null
  id: resource_c7b6bd39
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: reu_fpanv_m_gdo_20230101_20231221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "R\xE9union: Copernicus Vegetation Index Anomaly (FAPAR Anomaly) (Data\
    \ from 2022-01-01 to 2022-12-31)"
  download_url: https://data.humdata.org/dataset/5d29e2a9-6ca9-4d94-a562-7d3595ce54c3/resource/a7dd4365-8018-4238-8e3f-80c134af39dc/download/reu_fpanv_m_gdo_20220101_20221221_t.zip
  format: null
  id: resource_a7dd4365
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: reu_fpanv_m_gdo_20220101_20221221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "R\xE9union: Copernicus Vegetation Index Anomaly (FAPAR Anomaly) (Data\
    \ from 2021-01-01 to 2021-12-31)"
  download_url: https://data.humdata.org/dataset/5d29e2a9-6ca9-4d94-a562-7d3595ce54c3/resource/4a0d8665-dc88-4482-a6b0-e055dff2987b/download/reu_fpanv_m_gdo_20210101_20211221_t.zip
  format: null
  id: resource_4a0d8665
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: reu_fpanv_m_gdo_20210101_20211221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "R\xE9union: Copernicus Vegetation Index Anomaly (FAPAR Anomaly) (Data\
    \ from 2020-01-01 to 2020-12-31)"
  download_url: https://data.humdata.org/dataset/5d29e2a9-6ca9-4d94-a562-7d3595ce54c3/resource/fbf38fd7-80ab-4d09-8614-c85a95bb4a3a/download/reu_fpanv_m_gdo_20200101_20201221_t.zip
  format: null
  id: resource_fbf38fd7
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: reu_fpanv_m_gdo_20200101_20201221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "R\xE9union: Copernicus Vegetation Index Anomaly (FAPAR Anomaly) (Data\
    \ from 2019-01-01 to 2019-12-31)"
  download_url: https://data.humdata.org/dataset/5d29e2a9-6ca9-4d94-a562-7d3595ce54c3/resource/80d2738e-2ea8-4123-b910-1f9fd24df2ce/download/reu_fpanv_m_gdo_20190101_20191221_t.zip
  format: null
  id: resource_80d2738e
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: reu_fpanv_m_gdo_20190101_20191221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "R\xE9union: Copernicus Vegetation Index Anomaly (FAPAR Anomaly) (Data\
    \ from 2018-01-01 to 2018-12-31)"
  download_url: https://data.humdata.org/dataset/5d29e2a9-6ca9-4d94-a562-7d3595ce54c3/resource/ebd153bd-7d5c-44df-8c73-67b207c6e675/download/reu_fpanv_m_gdo_20180101_20181221_t.zip
  format: null
  id: resource_ebd153bd
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: reu_fpanv_m_gdo_20180101_20181221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "R\xE9union: Copernicus Vegetation Index Anomaly (FAPAR Anomaly) (Data\
    \ from 2017-01-01 to 2017-12-31)"
  download_url: https://data.humdata.org/dataset/5d29e2a9-6ca9-4d94-a562-7d3595ce54c3/resource/9d1302f5-e568-4ad1-abe3-9c117d8ab61a/download/reu_fpanv_m_gdo_20170101_20171221_t.zip
  format: null
  id: resource_9d1302f5
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: reu_fpanv_m_gdo_20170101_20171221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "R\xE9union: Copernicus Vegetation Index Anomaly (FAPAR Anomaly) (Data\
    \ from 2016-01-01 to 2016-12-31)"
  download_url: https://data.humdata.org/dataset/5d29e2a9-6ca9-4d94-a562-7d3595ce54c3/resource/5315c82d-7c8d-4323-bcfa-fca3a1004608/download/reu_fpanv_m_gdo_20160101_20161221_t.zip
  format: null
  id: resource_5315c82d
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: reu_fpanv_m_gdo_20160101_20161221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "R\xE9union: Copernicus Vegetation Index Anomaly (FAPAR Anomaly) (Data\
    \ from 2015-01-01 to 2015-12-31)"
  download_url: https://data.humdata.org/dataset/5d29e2a9-6ca9-4d94-a562-7d3595ce54c3/resource/373c68c5-bb11-49e9-8f00-a19a66110e19/download/reu_fpanv_m_gdo_20150101_20151221_t.zip
  format: null
  id: resource_373c68c5
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: reu_fpanv_m_gdo_20150101_20151221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "R\xE9union: Copernicus Vegetation Index Anomaly (FAPAR Anomaly) (Data\
    \ from 2014-01-01 to 2014-12-31)"
  download_url: https://data.humdata.org/dataset/5d29e2a9-6ca9-4d94-a562-7d3595ce54c3/resource/ca0fb6e1-5ba8-4c16-bb79-1bb299b97328/download/reu_fpanv_m_gdo_20140101_20141221_t.zip
  format: null
  id: resource_ca0fb6e1
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: reu_fpanv_m_gdo_20140101_20141221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "R\xE9union: Copernicus Vegetation Index Anomaly (FAPAR Anomaly) (Data\
    \ from 2013-01-01 to 2013-12-31)"
  download_url: https://data.humdata.org/dataset/5d29e2a9-6ca9-4d94-a562-7d3595ce54c3/resource/dfe647c7-febc-471f-b92b-3652f3c796db/download/reu_fpanv_m_gdo_20130101_20131221_t.zip
  format: null
  id: resource_dfe647c7
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: reu_fpanv_m_gdo_20130101_20131221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "R\xE9union: Copernicus Vegetation Index Anomaly (FAPAR Anomaly) (Data\
    \ from 2012-01-21 to 2012-12-31)"
  download_url: https://data.humdata.org/dataset/5d29e2a9-6ca9-4d94-a562-7d3595ce54c3/resource/fc3afe2b-7d75-41c3-bef1-f277fee04fbe/download/reu_fpanv_m_gdo_20120121_20121221_t.zip
  format: null
  id: resource_fc3afe2b
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: reu_fpanv_m_gdo_20120121_20121221_t.zip
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-reu_copernicus_reunionvegetationindexano_2012
spatial:
  bbox: null
  centroid: null
  countries:
  - REU
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2026-01-10'
  start: '2012-01-21'
temporal_resolution: null
title: "R\xE9union: Copernicus Vegetation Index Anomaly (FAPAR Anomaly)"
version: null
vulnerability: null
---
