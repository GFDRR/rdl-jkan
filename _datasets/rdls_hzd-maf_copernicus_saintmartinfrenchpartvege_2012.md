---
attributions:
- entity:
    affiliation: null
    email: null
    name: European Commission, Joint Research Centre (JRC)
    url: https://data.humdata.org/dataset/maf-anomalies-fapar-viirs
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Copernicus
  url: https://data.humdata.org/dataset/maf-anomalies-fapar-viirs
creator:
  affiliation: null
  email: null
  name: Copernicus
  url: https://data.humdata.org/dataset/maf-anomalies-fapar-viirs
dataset_id: rdls_hzd-maf_copernicus_saintmartinfrenchpartvege_2012
description: 'Fraction of Absorbed Photosynthetically Active Radiation (FAPAR) is
  a biophysical dimensionless quantity (its values range from 0/no absorption to 1/total
  absorption) used to assess the greenness and health of vegetation. FAPAR anomalies
  can be used as an indicator to detect and monitor the impacts of agricultural drought
  on the growth and productivity of vegetation. The data is presented in 10-day time
  composite of the Visible Infrared Imaging Radiometer Suite (VIIRS).. [Source: This
  metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/maf-anomalies-fapar-viirs]'
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
  description: FAPAR values from VIIRS satellite observations are collected in 10-day
    composites. Anomalies are calculated at each grid cell as the deviation from a
    long-term mean baseline (2012 to last available full year), producing raster datasets
    that serve as indicators of agricultural drought stress on vegetation growth and
    productivity.
  sources:
  - id: source_1
    license: null
    name: European Commission, Joint Research Centre (JRC)
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
  - id: source_2
    license: null
    name: Copernicus
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/maf-anomalies-fapar-viirs
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
  description: 'Saint Martin (French part): Copernicus Vegetation Index Anomaly (FAPAR
    Anomaly) (Data from 2026-01-01 to 2026-01-10)'
  download_url: https://data.humdata.org/dataset/ab106064-a78c-4bba-862e-eef1d7f2243a/resource/17b6cd47-05bc-49be-98fd-50722719f140/download/maf_fpanv_m_gdo_20260101_20260101_t.zip
  format: null
  id: resource_17b6cd47
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: maf_fpanv_m_gdo_20260101_20260101_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Saint Martin (French part): Copernicus Vegetation Index Anomaly (FAPAR
    Anomaly) (Data from 2025-01-01 to 2025-12-31)'
  download_url: https://data.humdata.org/dataset/ab106064-a78c-4bba-862e-eef1d7f2243a/resource/aaf90c10-1a36-45ec-942e-964a32f8b2b3/download/maf_fpanv_m_gdo_20250101_20251221_t.zip
  format: null
  id: resource_aaf90c10
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: maf_fpanv_m_gdo_20250101_20251221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Saint Martin (French part): Copernicus Vegetation Index Anomaly (FAPAR
    Anomaly) (Data from 2024-01-01 to 2024-12-31)'
  download_url: https://data.humdata.org/dataset/ab106064-a78c-4bba-862e-eef1d7f2243a/resource/3786948a-88c9-4041-a3db-b328e78a044b/download/maf_fpanv_m_gdo_20240101_20241221_t.zip
  format: null
  id: resource_3786948a
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: maf_fpanv_m_gdo_20240101_20241221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Saint Martin (French part): Copernicus Vegetation Index Anomaly (FAPAR
    Anomaly) (Data from 2023-01-01 to 2023-12-31)'
  download_url: https://data.humdata.org/dataset/ab106064-a78c-4bba-862e-eef1d7f2243a/resource/a314fa10-5894-42f7-aaab-d2774ff9e11e/download/maf_fpanv_m_gdo_20230101_20231221_t.zip
  format: null
  id: resource_a314fa10
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: maf_fpanv_m_gdo_20230101_20231221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Saint Martin (French part): Copernicus Vegetation Index Anomaly (FAPAR
    Anomaly) (Data from 2022-01-01 to 2022-12-31)'
  download_url: https://data.humdata.org/dataset/ab106064-a78c-4bba-862e-eef1d7f2243a/resource/ea5be7bf-ccaf-4b7a-bb2b-ea20ae8bcffa/download/maf_fpanv_m_gdo_20220101_20221221_t.zip
  format: null
  id: resource_ea5be7bf
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: maf_fpanv_m_gdo_20220101_20221221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Saint Martin (French part): Copernicus Vegetation Index Anomaly (FAPAR
    Anomaly) (Data from 2021-01-01 to 2021-12-31)'
  download_url: https://data.humdata.org/dataset/ab106064-a78c-4bba-862e-eef1d7f2243a/resource/2257a152-896c-47bd-bdca-204f527667fa/download/maf_fpanv_m_gdo_20210101_20211221_t.zip
  format: null
  id: resource_2257a152
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: maf_fpanv_m_gdo_20210101_20211221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Saint Martin (French part): Copernicus Vegetation Index Anomaly (FAPAR
    Anomaly) (Data from 2020-01-01 to 2020-12-31)'
  download_url: https://data.humdata.org/dataset/ab106064-a78c-4bba-862e-eef1d7f2243a/resource/b19319a2-cf85-4684-8528-5941da9f494e/download/maf_fpanv_m_gdo_20200101_20201221_t.zip
  format: null
  id: resource_b19319a2
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: maf_fpanv_m_gdo_20200101_20201221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Saint Martin (French part): Copernicus Vegetation Index Anomaly (FAPAR
    Anomaly) (Data from 2019-01-01 to 2019-12-31)'
  download_url: https://data.humdata.org/dataset/ab106064-a78c-4bba-862e-eef1d7f2243a/resource/f719bf3d-1f8b-4877-bb3c-3c6807458823/download/maf_fpanv_m_gdo_20190101_20191221_t.zip
  format: null
  id: resource_f719bf3d
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: maf_fpanv_m_gdo_20190101_20191221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Saint Martin (French part): Copernicus Vegetation Index Anomaly (FAPAR
    Anomaly) (Data from 2018-01-01 to 2018-12-31)'
  download_url: https://data.humdata.org/dataset/ab106064-a78c-4bba-862e-eef1d7f2243a/resource/8d9f879b-6fe6-4853-aed3-7d74b53be541/download/maf_fpanv_m_gdo_20180101_20181221_t.zip
  format: null
  id: resource_8d9f879b
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: maf_fpanv_m_gdo_20180101_20181221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Saint Martin (French part): Copernicus Vegetation Index Anomaly (FAPAR
    Anomaly) (Data from 2017-01-01 to 2017-12-31)'
  download_url: https://data.humdata.org/dataset/ab106064-a78c-4bba-862e-eef1d7f2243a/resource/adde9e49-6938-4ba9-a4d3-7d645559127f/download/maf_fpanv_m_gdo_20170101_20171221_t.zip
  format: null
  id: resource_adde9e49
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: maf_fpanv_m_gdo_20170101_20171221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Saint Martin (French part): Copernicus Vegetation Index Anomaly (FAPAR
    Anomaly) (Data from 2016-01-01 to 2016-12-31)'
  download_url: https://data.humdata.org/dataset/ab106064-a78c-4bba-862e-eef1d7f2243a/resource/cc28ada6-1390-4f05-9237-5db7a9ad279e/download/maf_fpanv_m_gdo_20160101_20161221_t.zip
  format: null
  id: resource_cc28ada6
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: maf_fpanv_m_gdo_20160101_20161221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Saint Martin (French part): Copernicus Vegetation Index Anomaly (FAPAR
    Anomaly) (Data from 2015-01-01 to 2015-12-31)'
  download_url: https://data.humdata.org/dataset/ab106064-a78c-4bba-862e-eef1d7f2243a/resource/7787d442-e54c-4c60-a7c9-9b76ff1f1689/download/maf_fpanv_m_gdo_20150101_20151221_t.zip
  format: null
  id: resource_7787d442
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: maf_fpanv_m_gdo_20150101_20151221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Saint Martin (French part): Copernicus Vegetation Index Anomaly (FAPAR
    Anomaly) (Data from 2014-01-01 to 2014-12-31)'
  download_url: https://data.humdata.org/dataset/ab106064-a78c-4bba-862e-eef1d7f2243a/resource/807b18c1-14c3-4de7-a887-503c57726fa1/download/maf_fpanv_m_gdo_20140101_20141221_t.zip
  format: null
  id: resource_807b18c1
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: maf_fpanv_m_gdo_20140101_20141221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Saint Martin (French part): Copernicus Vegetation Index Anomaly (FAPAR
    Anomaly) (Data from 2013-01-01 to 2013-12-31)'
  download_url: https://data.humdata.org/dataset/ab106064-a78c-4bba-862e-eef1d7f2243a/resource/d64c5af6-d142-4ffb-a13e-84efdecc1722/download/maf_fpanv_m_gdo_20130101_20131221_t.zip
  format: null
  id: resource_d64c5af6
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: maf_fpanv_m_gdo_20130101_20131221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Saint Martin (French part): Copernicus Vegetation Index Anomaly (FAPAR
    Anomaly) (Data from 2012-01-21 to 2012-12-31)'
  download_url: https://data.humdata.org/dataset/ab106064-a78c-4bba-862e-eef1d7f2243a/resource/087d2edd-7c9c-4b64-9e75-67d13009ad22/download/maf_fpanv_m_gdo_20120121_20121221_t.zip
  format: null
  id: resource_087d2edd
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: maf_fpanv_m_gdo_20120121_20121221_t.zip
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-maf_copernicus_saintmartinfrenchpartvege_2012
spatial:
  bbox: null
  centroid: null
  countries:
  - MAF
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2026-01-10'
  start: '2012-01-21'
temporal_resolution: null
title: 'Saint Martin (French part): Copernicus Vegetation Index Anomaly (FAPAR Anomaly)'
version: null
vulnerability: null
---
