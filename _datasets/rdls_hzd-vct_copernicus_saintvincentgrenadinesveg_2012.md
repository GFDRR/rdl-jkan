---
attributions:
- entity:
    affiliation: null
    email: null
    name: Copernicus Vegetation Index (VIIRS)
    url: https://data.humdata.org/dataset/vct-anomalies-fapar-viirs
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Copernicus
  url: https://data.humdata.org/dataset/vct-anomalies-fapar-viirs
creator:
  affiliation: null
  email: null
  name: Copernicus
  url: https://data.humdata.org/dataset/vct-anomalies-fapar-viirs
dataset_id: rdls_hzd-vct_copernicus_saintvincentgrenadinesveg_2012
description: 'Fraction of Absorbed Photosynthetically Active Radiation (FAPAR) is
  a biophysical dimensionless quantity (its values range from 0/no absorption to 1/total
  absorption) used to assess the greenness and health of vegetation. FAPAR anomalies
  can be used as an indicator to detect and monitor the impacts of agricultural drought
  on the growth and productivity of vegetation. The data is presented in 10-day time
  composite of the Visible Infrared Imaging Radiometer Suite (VIIRS).. [Source: This
  metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/vct-anomalies-fapar-viirs]'
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
  description: FAPAR values from VIIRS satellite observations are collected at 10-day
    intervals. Anomalies are calculated by computing the deviation of each grid cell's
    FAPAR value from its long-term mean (baseline 2012 to last complete year), producing
    raster datasets that serve as an empirical indicator of agricultural drought stress
    on vegetation.
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
- href: https://data.humdata.org/dataset/vct-anomalies-fapar-viirs
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
  description: 'Saint Vincent and the Grenadines: Copernicus Vegetation Index Anomaly
    (FAPAR Anomaly) (Data from 2026-01-01 to 2026-01-10)'
  download_url: https://data.humdata.org/dataset/c07cbf9c-15af-4f12-ba50-1d5948177aa3/resource/d28237ee-cf5e-4220-ae3c-21ea39066ea3/download/vct_fpanv_m_gdo_20260101_20260101_t.zip
  format: null
  id: resource_d28237ee
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: vct_fpanv_m_gdo_20260101_20260101_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Saint Vincent and the Grenadines: Copernicus Vegetation Index Anomaly
    (FAPAR Anomaly) (Data from 2025-01-01 to 2025-12-31)'
  download_url: https://data.humdata.org/dataset/c07cbf9c-15af-4f12-ba50-1d5948177aa3/resource/a176e828-8623-4188-9778-8a12e4ef4e6e/download/vct_fpanv_m_gdo_20250101_20251221_t.zip
  format: null
  id: resource_a176e828
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: vct_fpanv_m_gdo_20250101_20251221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Saint Vincent and the Grenadines: Copernicus Vegetation Index Anomaly
    (FAPAR Anomaly) (Data from 2024-01-01 to 2024-12-31)'
  download_url: https://data.humdata.org/dataset/c07cbf9c-15af-4f12-ba50-1d5948177aa3/resource/2f29b7c5-2e10-4b10-8874-fa0261495042/download/vct_fpanv_m_gdo_20240101_20241221_t.zip
  format: null
  id: resource_2f29b7c5
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: vct_fpanv_m_gdo_20240101_20241221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Saint Vincent and the Grenadines: Copernicus Vegetation Index Anomaly
    (FAPAR Anomaly) (Data from 2023-01-01 to 2023-12-31)'
  download_url: https://data.humdata.org/dataset/c07cbf9c-15af-4f12-ba50-1d5948177aa3/resource/719221d9-6fd4-4a90-83ed-1d7d55f2697e/download/vct_fpanv_m_gdo_20230101_20231221_t.zip
  format: null
  id: resource_719221d9
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: vct_fpanv_m_gdo_20230101_20231221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Saint Vincent and the Grenadines: Copernicus Vegetation Index Anomaly
    (FAPAR Anomaly) (Data from 2022-01-01 to 2022-12-31)'
  download_url: https://data.humdata.org/dataset/c07cbf9c-15af-4f12-ba50-1d5948177aa3/resource/3146d7d5-b23d-4426-8c1d-1816db939b0b/download/vct_fpanv_m_gdo_20220101_20221221_t.zip
  format: null
  id: resource_3146d7d5
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: vct_fpanv_m_gdo_20220101_20221221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Saint Vincent and the Grenadines: Copernicus Vegetation Index Anomaly
    (FAPAR Anomaly) (Data from 2021-01-01 to 2021-12-31)'
  download_url: https://data.humdata.org/dataset/c07cbf9c-15af-4f12-ba50-1d5948177aa3/resource/5320d430-9f20-4886-bfb8-1851f14a4fd6/download/vct_fpanv_m_gdo_20210101_20211221_t.zip
  format: null
  id: resource_5320d430
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: vct_fpanv_m_gdo_20210101_20211221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Saint Vincent and the Grenadines: Copernicus Vegetation Index Anomaly
    (FAPAR Anomaly) (Data from 2020-01-01 to 2020-12-31)'
  download_url: https://data.humdata.org/dataset/c07cbf9c-15af-4f12-ba50-1d5948177aa3/resource/d581edec-b095-496e-98d3-c57a3dd7986d/download/vct_fpanv_m_gdo_20200101_20201221_t.zip
  format: null
  id: resource_d581edec
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: vct_fpanv_m_gdo_20200101_20201221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Saint Vincent and the Grenadines: Copernicus Vegetation Index Anomaly
    (FAPAR Anomaly) (Data from 2019-01-01 to 2019-12-31)'
  download_url: https://data.humdata.org/dataset/c07cbf9c-15af-4f12-ba50-1d5948177aa3/resource/c146fe7c-9213-4355-811d-466c83ed0694/download/vct_fpanv_m_gdo_20190101_20191221_t.zip
  format: null
  id: resource_c146fe7c
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: vct_fpanv_m_gdo_20190101_20191221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Saint Vincent and the Grenadines: Copernicus Vegetation Index Anomaly
    (FAPAR Anomaly) (Data from 2018-01-01 to 2018-12-31)'
  download_url: https://data.humdata.org/dataset/c07cbf9c-15af-4f12-ba50-1d5948177aa3/resource/73d826c9-7f93-419e-b868-6f6ca7cc8f93/download/vct_fpanv_m_gdo_20180101_20181221_t.zip
  format: null
  id: resource_73d826c9
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: vct_fpanv_m_gdo_20180101_20181221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Saint Vincent and the Grenadines: Copernicus Vegetation Index Anomaly
    (FAPAR Anomaly) (Data from 2017-01-01 to 2017-12-31)'
  download_url: https://data.humdata.org/dataset/c07cbf9c-15af-4f12-ba50-1d5948177aa3/resource/f609c814-1fab-444e-bdce-868eec46d7d5/download/vct_fpanv_m_gdo_20170101_20171221_t.zip
  format: null
  id: resource_f609c814
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: vct_fpanv_m_gdo_20170101_20171221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Saint Vincent and the Grenadines: Copernicus Vegetation Index Anomaly
    (FAPAR Anomaly) (Data from 2016-01-01 to 2016-12-31)'
  download_url: https://data.humdata.org/dataset/c07cbf9c-15af-4f12-ba50-1d5948177aa3/resource/23440646-b296-4178-9494-b463727e8ab8/download/vct_fpanv_m_gdo_20160101_20161221_t.zip
  format: null
  id: resource_23440646
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: vct_fpanv_m_gdo_20160101_20161221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Saint Vincent and the Grenadines: Copernicus Vegetation Index Anomaly
    (FAPAR Anomaly) (Data from 2015-01-01 to 2015-12-31)'
  download_url: https://data.humdata.org/dataset/c07cbf9c-15af-4f12-ba50-1d5948177aa3/resource/4a45e7c3-ad28-40b5-9eb8-3d34c9817c7f/download/vct_fpanv_m_gdo_20150101_20151221_t.zip
  format: null
  id: resource_4a45e7c3
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: vct_fpanv_m_gdo_20150101_20151221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Saint Vincent and the Grenadines: Copernicus Vegetation Index Anomaly
    (FAPAR Anomaly) (Data from 2014-01-01 to 2014-12-31)'
  download_url: https://data.humdata.org/dataset/c07cbf9c-15af-4f12-ba50-1d5948177aa3/resource/0e815788-a67a-48d3-a420-64a806c49a0a/download/vct_fpanv_m_gdo_20140101_20141221_t.zip
  format: null
  id: resource_0e815788
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: vct_fpanv_m_gdo_20140101_20141221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Saint Vincent and the Grenadines: Copernicus Vegetation Index Anomaly
    (FAPAR Anomaly) (Data from 2013-01-01 to 2013-12-31)'
  download_url: https://data.humdata.org/dataset/c07cbf9c-15af-4f12-ba50-1d5948177aa3/resource/73b4b0c9-9f63-4412-b1f6-2c4b059536cc/download/vct_fpanv_m_gdo_20130101_20131221_t.zip
  format: null
  id: resource_73b4b0c9
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: vct_fpanv_m_gdo_20130101_20131221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Saint Vincent and the Grenadines: Copernicus Vegetation Index Anomaly
    (FAPAR Anomaly) (Data from 2012-01-21 to 2012-12-31)'
  download_url: https://data.humdata.org/dataset/c07cbf9c-15af-4f12-ba50-1d5948177aa3/resource/cc583b68-4805-47c6-b00b-198e5a7c4906/download/vct_fpanv_m_gdo_20120121_20121221_t.zip
  format: null
  id: resource_cc583b68
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: vct_fpanv_m_gdo_20120121_20121221_t.zip
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-vct_copernicus_saintvincentgrenadinesveg_2012
spatial:
  bbox: null
  centroid: null
  countries:
  - VCT
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2026-01-10'
  start: '2012-01-21'
temporal_resolution: null
title: 'Saint Vincent and the Grenadines: Copernicus Vegetation Index Anomaly (FAPAR
  Anomaly)'
version: null
vulnerability: null
---
