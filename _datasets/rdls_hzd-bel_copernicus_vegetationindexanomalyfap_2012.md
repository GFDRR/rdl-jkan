---
attributions:
- entity:
    affiliation: null
    email: null
    name: Copernicus Vegetation Index (VIIRS)
    url: https://data.humdata.org/dataset/bel-anomalies-fapar-viirs
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: European Commission, Joint Research Centre (JRC)
    url: https://data.humdata.org/dataset/bel-anomalies-fapar-viirs
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Copernicus
  url: https://data.humdata.org/dataset/bel-anomalies-fapar-viirs
creator:
  affiliation: null
  email: null
  name: Copernicus
  url: https://data.humdata.org/dataset/bel-anomalies-fapar-viirs
dataset_id: rdls_hzd-bel_copernicus_vegetationindexanomalyfap_2012
description: 'Fraction of Absorbed Photosynthetically Active Radiation (FAPAR) is
  a biophysical dimensionless quantity (its values range from 0/no absorption to 1/total
  absorption) used to assess the greenness and health of vegetation. FAPAR anomalies
  can be used as an indicator to detect and monitor the impacts of agricultural drought
  on the growth and productivity of vegetation. The data is presented in 10-day time
  composite of the Visible Infrared Imaging Radiometer Suite (VIIRS).. [Source: This
  metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/bel-anomalies-fapar-viirs]'
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
  description: VIIRS satellite observations of FAPAR are collected at 10-day intervals
    and processed by the JRC to calculate anomalies as deviations from a long-term
    mean baseline (2012 to the last available full year). The resulting raster grids
    are distributed as annual GeoTIFF composites to enable temporal monitoring of
    agricultural drought impacts on vegetation productivity across Belgium.
  sources:
  - id: source_1
    license: null
    name: Copernicus Vegetation Index (VIIRS)
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
  - id: source_2
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
- href: https://data.humdata.org/dataset/bel-anomalies-fapar-viirs
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
  description: 'Belgium: Copernicus Vegetation Index Anomaly (FAPAR Anomaly) (Data
    from 2026-01-01 to 2026-01-10)'
  download_url: https://data.humdata.org/dataset/65c3ec70-99e1-4a38-95e7-bb1e8f9208d2/resource/cc67107f-969e-4ce6-9ba2-4f2dc906927c/download/bel_fpanv_m_gdo_20260101_20260101_t.zip
  format: null
  id: resource_cc67107f
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bel_fpanv_m_gdo_20260101_20260101_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Belgium: Copernicus Vegetation Index Anomaly (FAPAR Anomaly) (Data
    from 2025-01-01 to 2025-12-31)'
  download_url: https://data.humdata.org/dataset/65c3ec70-99e1-4a38-95e7-bb1e8f9208d2/resource/fdcd8f25-33a8-4bea-8761-8c23e8a971e3/download/bel_fpanv_m_gdo_20250101_20251221_t.zip
  format: null
  id: resource_fdcd8f25
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bel_fpanv_m_gdo_20250101_20251221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Belgium: Copernicus Vegetation Index Anomaly (FAPAR Anomaly) (Data
    from 2024-01-01 to 2024-12-31)'
  download_url: https://data.humdata.org/dataset/65c3ec70-99e1-4a38-95e7-bb1e8f9208d2/resource/e279680d-eeeb-4c7f-b69c-3fd4bd7e141d/download/bel_fpanv_m_gdo_20240101_20241221_t.zip
  format: null
  id: resource_e279680d
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bel_fpanv_m_gdo_20240101_20241221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Belgium: Copernicus Vegetation Index Anomaly (FAPAR Anomaly) (Data
    from 2023-01-01 to 2023-12-31)'
  download_url: https://data.humdata.org/dataset/65c3ec70-99e1-4a38-95e7-bb1e8f9208d2/resource/161474c5-34c4-4dd1-962c-32a0844fb738/download/bel_fpanv_m_gdo_20230101_20231221_t.zip
  format: null
  id: resource_161474c5
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bel_fpanv_m_gdo_20230101_20231221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Belgium: Copernicus Vegetation Index Anomaly (FAPAR Anomaly) (Data
    from 2022-01-01 to 2022-12-31)'
  download_url: https://data.humdata.org/dataset/65c3ec70-99e1-4a38-95e7-bb1e8f9208d2/resource/c4defb9a-b227-4a3e-822d-4045f5a7ef98/download/bel_fpanv_m_gdo_20220101_20221221_t.zip
  format: null
  id: resource_c4defb9a
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bel_fpanv_m_gdo_20220101_20221221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Belgium: Copernicus Vegetation Index Anomaly (FAPAR Anomaly) (Data
    from 2021-01-01 to 2021-12-31)'
  download_url: https://data.humdata.org/dataset/65c3ec70-99e1-4a38-95e7-bb1e8f9208d2/resource/a4811744-0ae9-484e-8877-bdfba2c2ea2b/download/bel_fpanv_m_gdo_20210101_20211221_t.zip
  format: null
  id: resource_a4811744
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bel_fpanv_m_gdo_20210101_20211221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Belgium: Copernicus Vegetation Index Anomaly (FAPAR Anomaly) (Data
    from 2020-01-01 to 2020-12-31)'
  download_url: https://data.humdata.org/dataset/65c3ec70-99e1-4a38-95e7-bb1e8f9208d2/resource/b7dfb123-4aa1-43e6-b7b4-cb5148cac9c9/download/bel_fpanv_m_gdo_20200101_20201221_t.zip
  format: null
  id: resource_b7dfb123
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bel_fpanv_m_gdo_20200101_20201221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Belgium: Copernicus Vegetation Index Anomaly (FAPAR Anomaly) (Data
    from 2019-01-01 to 2019-12-31)'
  download_url: https://data.humdata.org/dataset/65c3ec70-99e1-4a38-95e7-bb1e8f9208d2/resource/522f4612-519f-4239-82da-12eb4539422b/download/bel_fpanv_m_gdo_20190101_20191221_t.zip
  format: null
  id: resource_522f4612
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bel_fpanv_m_gdo_20190101_20191221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Belgium: Copernicus Vegetation Index Anomaly (FAPAR Anomaly) (Data
    from 2018-01-01 to 2018-12-31)'
  download_url: https://data.humdata.org/dataset/65c3ec70-99e1-4a38-95e7-bb1e8f9208d2/resource/c12c439f-d898-4a7c-9155-260d023698ad/download/bel_fpanv_m_gdo_20180101_20181221_t.zip
  format: null
  id: resource_c12c439f
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bel_fpanv_m_gdo_20180101_20181221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Belgium: Copernicus Vegetation Index Anomaly (FAPAR Anomaly) (Data
    from 2017-01-01 to 2017-12-31)'
  download_url: https://data.humdata.org/dataset/65c3ec70-99e1-4a38-95e7-bb1e8f9208d2/resource/d2be46cc-8ee6-43aa-a6bc-090e93f14ed2/download/bel_fpanv_m_gdo_20170101_20171221_t.zip
  format: null
  id: resource_d2be46cc
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bel_fpanv_m_gdo_20170101_20171221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Belgium: Copernicus Vegetation Index Anomaly (FAPAR Anomaly) (Data
    from 2016-01-01 to 2016-12-31)'
  download_url: https://data.humdata.org/dataset/65c3ec70-99e1-4a38-95e7-bb1e8f9208d2/resource/15f5ae38-9159-4447-8861-484916ad4409/download/bel_fpanv_m_gdo_20160101_20161221_t.zip
  format: null
  id: resource_15f5ae38
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bel_fpanv_m_gdo_20160101_20161221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Belgium: Copernicus Vegetation Index Anomaly (FAPAR Anomaly) (Data
    from 2015-01-01 to 2015-12-31)'
  download_url: https://data.humdata.org/dataset/65c3ec70-99e1-4a38-95e7-bb1e8f9208d2/resource/93d298f8-3b65-4426-a601-b64682840fda/download/bel_fpanv_m_gdo_20150101_20151221_t.zip
  format: null
  id: resource_93d298f8
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bel_fpanv_m_gdo_20150101_20151221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Belgium: Copernicus Vegetation Index Anomaly (FAPAR Anomaly) (Data
    from 2014-01-01 to 2014-12-31)'
  download_url: https://data.humdata.org/dataset/65c3ec70-99e1-4a38-95e7-bb1e8f9208d2/resource/1578bf98-1a51-46b2-a3d2-608aca525958/download/bel_fpanv_m_gdo_20140101_20141221_t.zip
  format: null
  id: resource_1578bf98
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bel_fpanv_m_gdo_20140101_20141221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Belgium: Copernicus Vegetation Index Anomaly (FAPAR Anomaly) (Data
    from 2013-01-01 to 2013-12-31)'
  download_url: https://data.humdata.org/dataset/65c3ec70-99e1-4a38-95e7-bb1e8f9208d2/resource/671546aa-6a9e-46fc-bf9c-bcf645602a2b/download/bel_fpanv_m_gdo_20130101_20131221_t.zip
  format: null
  id: resource_671546aa
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bel_fpanv_m_gdo_20130101_20131221_t.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Belgium: Copernicus Vegetation Index Anomaly (FAPAR Anomaly) (Data
    from 2012-01-21 to 2012-12-31)'
  download_url: https://data.humdata.org/dataset/65c3ec70-99e1-4a38-95e7-bb1e8f9208d2/resource/57910887-573c-4c51-a2e5-67a244523dfd/download/bel_fpanv_m_gdo_20120121_20121221_t.zip
  format: null
  id: resource_57910887
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bel_fpanv_m_gdo_20120121_20121221_t.zip
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-bel_copernicus_vegetationindexanomalyfap_2012
spatial:
  bbox: null
  centroid: null
  countries:
  - BEL
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2026-01-10'
  start: '2012-01-21'
temporal_resolution: null
title: 'Belgium: Copernicus Vegetation Index Anomaly (FAPAR Anomaly)'
version: null
vulnerability: null
---
