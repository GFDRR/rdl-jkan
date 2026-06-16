---
attributions:
- entity:
    affiliation: null
    email: null
    name: WorldPop Research Group
    url: https://data.humdata.org/dataset/census-based-gridded-population-estimates-for-burkina-faso-2019
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: GRID3 (Geo-Referenced Infrastructure and Demographic Data for Development)
    url: https://data.humdata.org/dataset/census-based-gridded-population-estimates-for-burkina-faso-2019
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: GRID3
  url: https://data.humdata.org/dataset/census-based-gridded-population-estimates-for-burkina-faso-2019
creator:
  affiliation: null
  email: null
  name: GRID3
  url: https://data.humdata.org/dataset/census-based-gridded-population-estimates-for-burkina-faso-2019
dataset_id: rdls_exp-bfa_grid3_censusbasedgriddedpopulat
description: "These data were produced by the WorldPop Research Group at the University\
  \ of Southampton. This work is part of the GRID3 (Geo-Referenced Infrastructure\
  \ and Demographic Data for Development) project funded by the Bill and Melinda Gates\
  \ Foundation (BMGF) and the United Kingdom Foreign, Commonwealth & Development Office\
  \ (OPP1182425). Project partners include WorldPop at the University of Southampton,\
  \ the United Nations Population Fund ( UNFPA ), Center for International Earth Science\
  \ Information Network ( CIESIN ) in the Earth Institute at Columbia University,\
  \ and the Flowminder Foundation. The Burkina Faso Institut National de la Statistique\
  \ et de la D\xE9mographie supported, facilitated this work, reviewed the results\
  \ and provided the census database. The modelling work, geospatial data processing,\
  \ and stakeholder engagement was led by Edith Darin. Support for the statistical\
  \ modelling was provided by Gianluca Boo, Claire A. Dooley, Douglas R. Leasure and\
  \ Chris W. Jochem. Support for the engagement work and review of the methods was\
  \ offered by Mathias Ku\xE9pi\xE9. Oversight was done by Andrew J. Tatem and Attila\
  \ N. Lazar. Recommended citation: WorldPop and Institut National de la Statistique\
  \ et de la D\xE9mographie du Burkina Faso. 2021. Census based gridded population\
  \ estimates for Burkina Faso (2019), version 1.0. WorldPop, University of Southampton.\
  \ doi:10.5258/SOTON/WP00687. [Source: This metadata record was automatically extracted\
  \ from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/census-based-gridded-population-estimates-for-burkina-faso-2019]"
details: "__Recommended citation:__ _WorldPop and Institut National de la Statistique\
  \ et de la D\xE9mographie du Burkina Faso. 2021. Census based gridded population\
  \ estimates for Burkina Faso (2019), version 1.0. WorldPop, University of Southampton.\
  \ doi:10.5258/SOTON/WP00687_ For further details, please, read BFA_population_v1_0_methods.pdf\
  \ Contact release@worldpop.org for more information."
exposure:
- asset_type:
    description: Gridded census-based population estimates for Burkina Faso at fine
      spatial resolution, including age-sex disaggregation
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
  description: Census data from Burkina Faso were processed by WorldPop using spatial
    modeling techniques to produce gridded population estimates at fine resolution.
    The dataset includes total population and age-sex disaggregated estimates distributed
    across a master grid covering the entire country, enabling spatial analysis of
    population distribution for development and risk assessment applications.
  sources:
  - id: source_1
    license: null
    name: WorldPop Research Group
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
  - id: source_2
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
- href: https://data.humdata.org/dataset/census-based-gridded-population-estimates-for-burkina-faso-2019
  rel: source
loss: null
project: null
publisher:
  affiliation: null
  email: null
  name: Humanitarian Data Exchange (HDX)
  url: https://data.humdata.org/
purpose: Census
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Gridded population estimates (~100m) for Burkina Faso. This geotiff
    raster contains estimates of total population size for each approximately 100
    m grid cell across the study area.
  download_url: https://wopr.worldpop.org/download/251
  format: null
  id: resource_28301977
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: BFA_population_v1_0_gridded.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Bottom-up gridded population estimates (~100m) for specific age-sex
    groups. This zip file contains geotiff rasters with estimates of population sizes
    for individual age-sex groups for each approximately 100 m grid cell across the
    study area.
  download_url: https://wopr.worldpop.org/download/250
  format: null
  id: resource_b241f7d1
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: BFA_population_v1_0_agesex.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Mastergrid for gridded population estimates. This geotiff raster contains
    the mastergrid used to define where population estimates were made. It contains
    a value of 1 where population estimates were made and a value of 0 or NA everywhere
    else. Cell IDs from the mastergrid can be used to lookup values in the SQL database.
  download_url: https://wopr.worldpop.org/download/252
  format: null
  id: resource_6bfe4154
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: BFA_population_v1_0_mastergrid.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Description of the methods used to produce the BFA v1.0 gridded population
    estimates. This pdf contains a technical report describing methods used to produce
    these gridded population estimates.
  download_url: https://wopr.worldpop.org/download/253
  format: null
  id: resource_a57b7af2
  media_type: application/pdf
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: BFA_population_v1_0_methods.pdf
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: BFA Population v1.0 (English + French). This README file provides information
    about the data included in the data release, how it was produced, source data
    that were used, and known assumptions and limitations of the results.
  download_url: https://wopr.worldpop.org/download/254
  format: null
  id: resource_c54b2c80
  media_type: application/pdf
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: BFA_population_v1_0_README.pdf
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: SQL database with Bayesian posterior population predictions. This SQLite
    database contains samples from the Bayesian posterior predictions of population
    size in each grid cell. The database can be used to develop applications that
    query the population estimates.
  download_url: https://wopr.worldpop.org/download/255
  format: SQL
  id: resource_8d55ef52
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: BFA_population_v1_0_sql.sql
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Supplementary files including data to reproduce the method. This zip
    file contains supplementary files including the data needed to reproduce the method.
  download_url: https://wopr.worldpop.org/download/256
  format: null
  id: resource_79e1268a
  media_type: application/pdf
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: BFA_population_v1_0_supplements.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Image tiles for gridded population estimates. These image tiles (XYZ
    format) allow for rapid display of the 100 m gridded population estimates across
    the study area in web applications.
  download_url: https://wopr.worldpop.org/download/257
  format: GIF
  id: resource_5ce94866
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: BFA_population_v1_0_tiles.zip
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-bfa_grid3_censusbasedgriddedpopulat
spatial:
  bbox: null
  centroid: null
  countries:
  - BFA
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal: null
temporal_resolution: null
title: Census-based gridded population estimates for Burkina Faso (2019), version
  1.0
version: null
vulnerability: null
---
