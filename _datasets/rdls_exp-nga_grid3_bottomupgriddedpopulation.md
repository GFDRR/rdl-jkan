---
attributions:
- entity:
    affiliation: null
    email: null
    name: GRID3 (Geo-Referenced Infrastructure and Demographic Data for Development)
    url: https://data.humdata.org/dataset/bottom-up-gridded-population-estimates-for-nigeria-version-2-0
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: GRID3
  url: https://data.humdata.org/dataset/bottom-up-gridded-population-estimates-for-nigeria-version-2-0
creator:
  affiliation: null
  email: null
  name: GRID3
  url: https://data.humdata.org/dataset/bottom-up-gridded-population-estimates-for-nigeria-version-2-0
dataset_id: rdls_exp-nga_grid3_bottomupgriddedpopulation
description: 'This data release provides gridded population estimates (spatial resolution
  of 3 arc-seconds, approximately 100 m grid cells) with national coverage for Nigeria,
  along with estimates of the number of people belonging to various age-sex groups.
  Version 2.0 is an update to the previous version 1.2 gridded population estimates
  and is based on more recent and detailed settlement information and a different
  regional boundary definition. These model-based population estimates most likely
  represent the time period around 2019, corresponding to the period when the satellite
  imagery was processed to generate building footprints. Populations are mapped only
  into areas where residential settlements are predicted. These data were produced
  by the WorldPop Research Group at the University of Southampton in collaboration
  with the National Population Commission of Nigeria. This work was part of the Geo-Referenced
  Infrastructure and Demographic Data for Development ( GRID3 ) programme with funding
  from the Bill and Melinda Gates Foundation and the United Kingdom''s Foreign, Commonwealth
  & Development Office (INV 009579, formerly OPP 1182425). Project partners included
  the United Nations Population Fund, Center for International Earth Science Information
  Network ( CIESIN ), a center within the Columbia Climate School at Columbia University,
  and the Flowminder Foundation. Statistical modelling was led by Chris Jochem and
  Doug Leasure additional support and oversight from Attila Lazar and Andy Tatem.
  Chris Lloyd provided the residential building classification. The microcensus data
  were originally collected by eHealth Africa and Oak Ridge National Laboratory with
  support from the Bill and Melinda Gates Foundation. The WorldPop grou and GRID3
  partners are acknowledged for their project support. RELEASE CONTENT NGA_population_v2_0_gridded.zip
  NGA_population_v2_0_admin.zip NGA_population_v2_0_sql.sql NGA_population_v2_0_mastergrid.tif
  NGA_population_v2_0_tiles.zip NGA_population_v2_0_agesex.zip LICENSE These data
  (1-6) may be redistributed using a Creative Commons Attribution 4.0 International
  (CC BY 4.0) License. Recommended citations WorldPop and National Population Commission
  of Nigeria. 2021. Bottom-up gridded population estimates for Nigeria, version 2.0.
  WorldPop, University of Southampton. doi: 10.5258/SOTON/WP00729. For further details,
  please, read NGA_population_v2_0_README.pdf. [Source: This metadata record was automatically
  extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/bottom-up-gridded-population-estimates-for-nigeria-version-2-0]'
details: '__Recommended citations__ _WorldPop and National Population Commission of
  Nigeria. 2021. Bottom-up gridded population estimates for Nigeria, version 2.0.
  WorldPop, University of Southampton. doi: 10.5258/SOTON/WP00729._'
exposure:
- asset_type:
    description: Gridded population estimates at 100m resolution with age-sex disaggregation
      for Nigeria
    id: population
    scheme: null
    title: null
    uri: null
  category: population
  id: exposure_1
  metrics:
  - dimension: population
    id: metric_1
    measurement:
      quantity_kind: count
      unit: count
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: Gridded population estimates were generated using satellite imagery
    and detailed settlement information processed around 2019, with spatial resolution
    of 3 arc-seconds (~100m grid cells). Version 2.0 incorporates more recent and
    detailed settlement data and updated regional boundary definitions compared to
    version 1.2. The dataset provides national coverage of Nigeria with population
    counts disaggregated by age-sex groups.
  sources:
  - id: source_1
    license: null
    name: GRID3 (Geo-Referenced Infrastructure and Demographic Data for Development)
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/bottom-up-gridded-population-estimates-for-nigeria-version-2-0
  rel: source
loss: null
project: null
publisher:
  affiliation: null
  email: null
  name: Humanitarian Data Exchange (HDX)
  url: https://data.humdata.org/
purpose: null
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: This README file provides information about the data included in the
    data release, how it was produced, source data that were used, and known assumptions
    and limitations of the results.
  download_url: https://wopr.worldpop.org/download/497
  format: null
  id: resource_6bd3b28f
  media_type: application/pdf
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: NGA_population_v2_0_README.pdf
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: This zip file contains a geotiff raster with estimates of total population
    size for each approximately 100 m grid cell across the study area. It also contains
    a geotiff raster with estimates of uncertainty in the population estimates.
  download_url: https://wopr.worldpop.org/download/495
  format: null
  id: resource_d68ec3a9
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: NGA_population_v2_0_gridded.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: This zip file contains geotiff rasters with estimates of population
    sizes for individual age-sex groups for each approximately 100 m grid cell across
    the study area.
  download_url: https://wopr.worldpop.org/download/499
  format: null
  id: resource_8db7ace6
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: NGA_population_v2_0_agesex.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: This geotiff raster contains the mastergrid used to define where population
    estimates were made. It contains a value of 1 where population estimates were
    made, i.e in grid cells considered as settled and a value of NA everywhere else.
    Cell IDs from the mastergrid can be used to lookup values in the SQL database.
  download_url: https://wopr.worldpop.org/download/501
  format: null
  id: resource_6190af26
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: NGA_population_v2_0_mastergrid.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: This zip file contains population totals for administrative units in
    Nigeria (i.e. states and local government areas). In addition, the gridded population
    estimates have been summarised to the Ward and Local Government Area (LGA) boundaries
    available from the GRID3 Nigeria Data Portal (https://grid3.gov.ng/). The boundaries
    are included as shapefiles with the population estimates included in the attribute
    tables. The population estimates are also included as .csv spreadsheets.
  download_url: https://wopr.worldpop.org/download/496
  format: PNG
  id: resource_b63e4ff0
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: NGA_population_v2_0_admin.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: This SQLite database contains samples from the Bayesian posterior predictions
    of population size in each grid cell. The database can be used to develop applications
    that query the population estimates.
  download_url: https://wopr.worldpop.org/download/498
  format: SQL
  id: resource_5807111f
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: NGA_population_v2_0_sql.sql
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: These image tiles (XYZ format) allow for rapid display of the 100 m
    gridded population estimates across the study area in web applications.
  download_url: https://wopr.worldpop.org/download/500
  format: PNG
  id: resource_c722b10a
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: NGA_population_v2_0_tiles.zip
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-nga_grid3_bottomupgriddedpopulation
spatial:
  bbox: null
  centroid: null
  countries:
  - NGA
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal: null
temporal_resolution: null
title: Bottom-up gridded population estimates for Nigeria, version 2.0
version: null
vulnerability: null
---
